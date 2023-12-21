from django.contrib import admin
from .models import Category, Product, Carousel, HTML_DIY, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}



# Register your model with the custom admin class
admin.site.register(HTML_DIY)

admin.site.register(Carousel)
admin.site.register(ProductImage)

