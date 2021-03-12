from django.contrib import admin
from basketapp.models import Basket

# admin.site.register(Basket)


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'sum')
    search_fields = ('user', )
    list_filter = ('product', )

    class Media:
        js = (
            "vendor/jquery/jquery.slim.min.js",
            "js/base-admin.js",
        )
