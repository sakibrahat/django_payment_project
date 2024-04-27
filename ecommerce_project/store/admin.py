# # store/admin.py
# from django.contrib import admin
# from .models import Product, Order

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'total_price', 'payment_status']
#     list_filter = ['payment_status']
#     actions = ['mark_as_paid']

#     def mark_as_paid(self, request, queryset):
#         updated_count = queryset.update(payment_status=True)
#         self.message_user(request, f'{updated_count} order(s) marked as paid.')

# admin.site.register(Product)
# admin.site.register(Order, OrderAdmin)
# store/admin.py
from django.contrib import admin
from .models import Product, Order
from django.http import HttpResponseRedirect


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_price', 'payment_status']
    list_filter = ['payment_status']
    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        updated_count = queryset.update(payment_status=True)
        self.message_user(request, f'{updated_count} order(s) marked as paid.')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    actions = ['add_custom_product']

    def add_custom_product(self, request, queryset):
        # Display a form to add a new product
        return HttpResponseRedirect('/admin/store/product/add/')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
