from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from catalog.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'image']
    search_fields = ['name', 'description']
    list_filter = ['category__name']

    def image(self, obj):
        return mark_safe(
            '<img src="{}" style="max-width: 100px; max-height: 100px;"/>'.format(obj.image_url)
        )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
