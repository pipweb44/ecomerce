from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from customers.models import Customer


def register_view(request):
    """صفحة التسجيل"""
    if request.user.is_authenticated:
        return redirect('products:home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # إنشاء ملف عميل مرتبط بالمستخدم
            Customer.objects.create(
                user=user,
                phone=request.POST.get('phone', ''),
                address=request.POST.get('address', ''),
                city=request.POST.get('city', '')
            )

            username = form.cleaned_data.get('username')
            messages.success(request, f'تم إنشاء حساب جديد للمستخدم {username}!')

            # تسجيل دخول تلقائي
            user = authenticate(username=username, password=form.cleaned_data.get('password1'))
            if user:
                login(request, user)
                return redirect('products:home')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile_view(request):
    """صفحة الملف الشخصي"""
    from orders.models import Order

    try:
        customer = request.user.customer
    except Customer.DoesNotExist:
        customer = Customer.objects.create(user=request.user)

    if request.method == 'POST':
        # تحديث بيانات المستخدم
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()

        # تحديث بيانات العميل
        customer.phone = request.POST.get('phone', '')
        customer.address = request.POST.get('address', '')
        customer.city = request.POST.get('city', '')
        customer.save()

        messages.success(request, 'تم تحديث بياناتك بنجاح!')
        return redirect('accounts:profile')

    # حساب إحصائيات الطلبات
    user_orders = Order.objects.filter(user=request.user)
    total_orders = user_orders.count()
    pending_orders = user_orders.filter(status='pending').count()
    delivered_orders = user_orders.filter(status='delivered').count()

    context = {
        'customer': customer,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def my_orders_view(request):
    """صفحة طلبات المستخدم"""
    from orders.models import Order

    # جلب طلبات المستخدم فقط
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    # حساب الإحصائيات
    pending_count = orders.filter(status='pending').count()
    shipped_count = orders.filter(status='shipped').count()
    delivered_count = orders.filter(status='delivered').count()

    context = {
        'orders': orders,
        'pending_count': pending_count,
        'shipped_count': shipped_count,
        'delivered_count': delivered_count,
    }
    return render(request, 'accounts/my_orders.html', context)


@login_required
def order_detail_view(request, order_id):
    """تفاصيل طلب محدد للمستخدم"""
    from orders.models import Order
    from django.shortcuts import get_object_or_404

    # التأكد من أن الطلب يخص المستخدم الحالي
    order = get_object_or_404(Order, id=order_id, user=request.user)

    context = {
        'order': order,
    }
    return render(request, 'accounts/order_detail.html', context)
