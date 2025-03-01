from django.contrib import admin
from .models import Category, Product


admin.site.site_header = "Custom Admin Panel"
admin.site.site_title = "Custom Admin"
admin.site.index_title = "Welcome to the Dashboard"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    ordering = ('created_at',)