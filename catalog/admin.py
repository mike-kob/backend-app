from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from catalog.models import Category, Product, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'descrshort', 'price', 'image']
    search_fields = ['name', 'description']
    list_filter = ['category__name']

    def image(self, obj):
        return mark_safe(
            '<img src="{}" style="max-width: 100px; max-height: 100px;"/>'.format(obj.image_url)
        )

    def descrshort(self, obj):
        out = obj.description
        return (out[:75] + '...') if len(out) > 75 else out


class OrderInline(admin.TabularInline):
    fields = ['product', 'id', 'quantity']

    model = Order.products.through
    verbose_name = u"Product"
    verbose_name_plural = u"Products"


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    exclude = ("products",)
    inlines = (
        OrderInline,
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
