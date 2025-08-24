from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="المستخدم")
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    address = models.TextField(blank=True, verbose_name="العنوان")
    city = models.CharField(max_length=50, blank=True, verbose_name="المدينة")
    postal_code = models.CharField(max_length=10, blank=True, verbose_name="الرمز البريدي")
    birth_date = models.DateField(null=True, blank=True, verbose_name="تاريخ الميلاد")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التسجيل")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    class Meta:
        verbose_name = "عميل"
        verbose_name_plural = "العملاء"
        ordering = ['-created_at']

    def __str__(self):
        if self.user:
            return f"{self.user.get_full_name() or self.user.username}"
        return f"عميل - {self.phone}"

    @property
    def full_name(self):
        if self.user:
            return self.user.get_full_name() or self.user.username
        return "غير محدد"

    @property
    def email(self):
        if self.user:
            return self.user.email
        return "غير محدد"
