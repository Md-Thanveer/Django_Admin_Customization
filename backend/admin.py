from django.contrib import admin
from .models import Category, Product

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
    readonly_fields = ('created_at',)
    list_editable = ('price', 'stock')

    fieldsets = (
        ('Basic Info', {'fields': ('name', 'category')}),
        ('Pricing & Stock', {'fields': ('price', 'stock')}),
    )

    def category_name(self, obj):
        return obj.category.name
    category_name.short_description = "Category"
