# from django.contrib import admin

# from django.contrib import admin
# from .models import Order, OrderItem

# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     extra = 0

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'full_name', 'email', 'address', 'paid', 'created_at', 'updated_at']
#     list_filter = ['paid', 'created_at', 'updated_at']
#     inlines = [OrderItemInline]

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ['order', 'product', 'price', 'quantity']

