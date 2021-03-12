from django.contrib import admin
from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'show_categories')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'categories')
    search_fields = ('name',)
    list_filter = ('categories', )
    filter_horizontal = ('categories', )

    @staticmethod
    def show_categories(obj):
        return ', '.join([category[1] for category in obj.categories.values_list()])
