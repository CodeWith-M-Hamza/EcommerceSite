from django.contrib import admin
from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'available', 'created_at', 'updated_at')
    list_filter = ('available', 'created_at', 'updated_at')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
