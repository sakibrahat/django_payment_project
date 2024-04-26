# store/admin.py
from django.contrib import admin
from .models import Product, Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_price', 'payment_status']
    list_filter = ['payment_status']
    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        updated_count = queryset.update(payment_status=True)
        self.message_user(request, f'{updated_count} order(s) marked as paid.')

admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
