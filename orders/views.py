from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from products.models import Product
from .models import Order, OrderItem
import json


def cart_view(request):
    """عرض سلة التسوق"""
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id, is_active=True)
            item_total = product.get_price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total': item_total
            })
            total += item_total
        except Product.DoesNotExist:
            continue

    context = {
        'cart_items': cart_items,
        'total': total,
        'cart_count': sum(cart.values())
    }
    return render(request, 'orders/cart.html', context)


@csrf_exempt
@require_POST
def add_to_cart(request):
    """إضافة منتج إلى السلة"""
    try:
        data = json.loads(request.body)
        product_id = str(data.get('product_id'))
        quantity = int(data.get('quantity', 1))

        product = get_object_or_404(Product, id=product_id, is_active=True)

        if quantity <= 0:
            return JsonResponse({'success': False, 'message': 'الكمية يجب أن تكون أكبر من صفر'})

        if quantity > product.stock_quantity:
            return JsonResponse({'success': False, 'message': 'الكمية المطلوبة غير متوفرة'})

        cart = request.session.get('cart', {})

        if product_id in cart:
            new_quantity = cart[product_id] + quantity
            if new_quantity > product.stock_quantity:
                return JsonResponse({'success': False, 'message': 'الكمية المطلوبة غير متوفرة'})
            cart[product_id] = new_quantity
        else:
            cart[product_id] = quantity

        request.session['cart'] = cart
        cart_count = sum(cart.values())

        return JsonResponse({
            'success': True,
            'message': 'تم إضافة المنتج إلى السلة',
            'cart_count': cart_count
        })

    except Exception as e:
        return JsonResponse({'success': False, 'message': 'حدث خطأ أثناء إضافة المنتج'})


@csrf_exempt
@require_POST
def update_cart(request):
    """تحديث كمية منتج في السلة"""
    try:
        data = json.loads(request.body)
        product_id = str(data.get('product_id'))
        quantity = int(data.get('quantity'))

        product = get_object_or_404(Product, id=product_id, is_active=True)
        cart = request.session.get('cart', {})

        if quantity <= 0:
            if product_id in cart:
                del cart[product_id]
        else:
            if quantity > product.stock_quantity:
                return JsonResponse({'success': False, 'message': 'الكمية المطلوبة غير متوفرة'})
            cart[product_id] = quantity

        request.session['cart'] = cart

        # حساب الإجمالي الجديد
        total = 0
        for pid, qty in cart.items():
            try:
                p = Product.objects.get(id=pid, is_active=True)
                total += p.get_price * qty
            except Product.DoesNotExist:
                continue

        return JsonResponse({
            'success': True,
            'cart_count': sum(cart.values()),
            'total': float(total)
        })

    except Exception as e:
        return JsonResponse({'success': False, 'message': 'حدث خطأ أثناء تحديث السلة'})


def checkout(request):
    """صفحة إتمام الطلب"""
    cart = request.session.get('cart', {})

    if not cart:
        messages.warning(request, 'سلة التسوق فارغة')
        return redirect('products:home')

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id, is_active=True)
            if quantity > product.stock_quantity:
                messages.error(request, f'الكمية المطلوبة من {product.name} غير متوفرة')
                return redirect('orders:cart')

            item_total = product.get_price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total': item_total
            })
            total += item_total
        except Product.DoesNotExist:
            continue

    if request.method == 'POST':
        # معالجة بيانات الطلب
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')
        shipping_address = request.POST.get('shipping_address')
        shipping_city = request.POST.get('shipping_city')
        shipping_postal_code = request.POST.get('shipping_postal_code', '')
        notes = request.POST.get('notes', '')

        # التحقق من البيانات
        if not all([customer_name, customer_email, customer_phone, shipping_address, shipping_city]):
            messages.error(request, 'يرجى ملء جميع الحقول المطلوبة')
            return render(request, 'orders/checkout.html', {
                'cart_items': cart_items,
                'total': total
            })

        # إنشاء الطلب
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            shipping_address=shipping_address,
            shipping_city=shipping_city,
            shipping_postal_code=shipping_postal_code,
            notes=notes,
            total_amount=total
        )

        # إنشاء عناصر الطلب
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['product'].get_price
            )

            # تقليل المخزون
            product = item['product']
            product.stock_quantity -= item['quantity']
            product.save()

        # مسح السلة
        request.session['cart'] = {}

        messages.success(request, f'تم إنشاء طلبك بنجاح. رقم الطلب: {order.order_number}')
        return redirect('orders:order_success', order_id=order.id)

    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'orders/checkout.html', context)


def order_success(request, order_id):
    """صفحة نجاح الطلب"""
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'orders/order_success.html', context)


def track_order(request):
    """تتبع الطلب"""
    order = None
    if request.method == 'POST':
        order_number = request.POST.get('order_number')
        try:
            # إذا كان المستخدم مسجل دخول، يمكنه رؤية طلباته فقط
            if request.user.is_authenticated:
                order = Order.objects.get(order_number=order_number, user=request.user)
            else:
                # للمستخدمين غير المسجلين، يمكنهم تتبع الطلبات بدون مستخدم
                order = Order.objects.get(order_number=order_number, user__isnull=True)
        except Order.DoesNotExist:
            if request.user.is_authenticated:
                messages.error(request, 'رقم الطلب غير صحيح أو لا يخصك')
            else:
                messages.error(request, 'رقم الطلب غير صحيح أو غير موجود')

    context = {'order': order}
    return render(request, 'orders/track_order.html', context)
