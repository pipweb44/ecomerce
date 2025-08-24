from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import uuid


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'في الانتظار'),
        ('confirmed', 'مؤكد'),
        ('processing', 'قيد التحضير'),
        ('shipped', 'تم الشحن'),
        ('delivered', 'تم التسليم'),
        ('cancelled', 'ملغي'),
        ('returned', 'مرتجع'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_number = models.CharField(max_length=20, unique=True, verbose_name="رقم الطلب")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='orders', verbose_name="المستخدم")

    # معلومات العميل
    customer_name = models.CharField(max_length=100, verbose_name="اسم العميل")
    customer_email = models.EmailField(verbose_name="البريد الإلكتروني")
    customer_phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")

    # عنوان التسليم
    shipping_address = models.TextField(verbose_name="عنوان التسليم")
    shipping_city = models.CharField(max_length=50, verbose_name="المدينة")
    shipping_postal_code = models.CharField(max_length=10, blank=True, verbose_name="الرمز البريدي")

    # معلومات الطلب
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending', verbose_name="حالة الطلب")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ الإجمالي")
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="تكلفة الشحن")
    notes = models.TextField(blank=True, verbose_name="ملاحظات")

    # تواريخ مهمة
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")
    confirmed_at = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ التأكيد")
    shipped_at = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ الشحن")
    delivered_at = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ التسليم")

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"
        ordering = ['-created_at']

    def __str__(self):
        return f"طلب #{self.order_number} - {self.customer_name}"

    def save(self, *args, **kwargs):
        if not self.order_number:
            # إنشاء رقم طلب فريد
            import random
            import string
            self.order_number = ''.join(random.choices(string.digits, k=8))
        super().save(*args, **kwargs)

    @property
    def get_total_with_shipping(self):
        """المبلغ الإجمالي مع الشحن"""
        return self.total_amount + self.shipping_cost

    @property
    def get_status_display_color(self):
        """لون حالة الطلب للعرض"""
        colors = {
            'pending': 'warning',
            'confirmed': 'info',
            'processing': 'primary',
            'shipped': 'secondary',
            'delivered': 'success',
            'cancelled': 'danger',
            'returned': 'dark',
        }
        return colors.get(self.status, 'secondary')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(verbose_name="الكمية")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الإجمالي")

    class Meta:
        verbose_name = "عنصر الطلب"
        verbose_name_plural = "عناصر الطلبات"

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity
        super().save(*args, **kwargs)


class OrderStatusHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='status_history', verbose_name="الطلب")
    status = models.CharField(max_length=20, choices=Order.ORDER_STATUS_CHOICES, verbose_name="الحالة")
    notes = models.TextField(blank=True, verbose_name="ملاحظات")
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="تم التغيير بواسطة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التغيير")

    class Meta:
        verbose_name = "تاريخ حالة الطلب"
        verbose_name_plural = "تاريخ حالات الطلبات"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.order.order_number} - {self.get_status_display()}"
