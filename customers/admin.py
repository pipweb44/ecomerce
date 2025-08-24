from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'city', 'created_at')
    list_filter = ('city', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'phone')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('معلومات المستخدم', {
            'fields': ('user',)
        }),
        ('معلومات الاتصال', {
            'fields': ('phone', 'address', 'city', 'postal_code')
        }),
        ('معلومات شخصية', {
            'fields': ('birth_date',)
        }),
        ('تواريخ', {
            'fields': ('created_at', 'updated_at')
        }),
    )
