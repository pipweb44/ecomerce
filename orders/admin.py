from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import Order, OrderItem, OrderStatusHistory


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('total',)
    fields = ('product', 'quantity', 'price', 'total')


class OrderStatusHistoryInline(admin.TabularInline):
    model = OrderStatusHistory
    extra = 0
    readonly_fields = ('created_at', 'changed_by')
    fields = ('status', 'notes', 'changed_by', 'created_at')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'customer_phone', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at', 'shipping_city')
    search_fields = ('order_number', 'customer_name', 'customer_email', 'customer_phone')
    readonly_fields = ('id', 'order_number', 'created_at', 'updated_at')
    list_editable = ('status',)
    inlines = [OrderItemInline, OrderStatusHistoryInline]

    fieldsets = (
        ('معلومات الطلب', {
            'fields': ('id', 'order_number', 'status', 'user')
        }),
        ('معلومات العميل', {
            'fields': ('customer_name', 'customer_email', 'customer_phone')
        }),
        ('عنوان التسليم', {
            'fields': ('shipping_address', 'shipping_city', 'shipping_postal_code')
        }),
        ('المبالغ', {
            'fields': ('total_amount', 'shipping_cost')
        }),
        ('ملاحظات وتواريخ', {
            'fields': ('notes', 'created_at', 'updated_at', 'confirmed_at', 'shipped_at', 'delivered_at')
        }),
    )

    def status_badge(self, obj):
        color = obj.get_status_display_color
        return format_html(
            '<span class="badge badge-{}">{}</span>',
            color,
            obj.get_status_display()
        )
    status_badge.short_description = 'حالة الطلب'

    def save_model(self, request, obj, form, change):
        if change:
            # تسجيل تغيير الحالة
            original = Order.objects.get(pk=obj.pk)
            if original.status != obj.status:
                # تحديث التواريخ حسب الحالة
                if obj.status == 'confirmed' and not obj.confirmed_at:
                    obj.confirmed_at = timezone.now()
                elif obj.status == 'shipped' and not obj.shipped_at:
                    obj.shipped_at = timezone.now()
                elif obj.status == 'delivered' and not obj.delivered_at:
                    obj.delivered_at = timezone.now()

                # إنشاء سجل في تاريخ الحالات
                OrderStatusHistory.objects.create(
                    order=obj,
                    status=obj.status,
                    changed_by=request.user,
                    notes=f"تم تغيير الحالة من {original.get_status_display()} إلى {obj.get_status_display()}"
                )

        super().save_model(request, obj, form, change)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'total')
    list_filter = ('order__status', 'order__created_at')
    search_fields = ('order__order_number', 'product__name')
    readonly_fields = ('total',)


@admin.register(OrderStatusHistory)
class OrderStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'changed_by', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order__order_number', 'notes')
    readonly_fields = ('created_at',)
