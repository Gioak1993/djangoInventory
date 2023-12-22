from django.contrib import admin
from .models import ProductInfo, Images

# Register your models here.

class ImagesInLine(admin.StackedInline):
    model = Images
    extra = 7

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title_text", "description_text", "condition", "price_number"]}),
        ("Item Specifics", {"fields": ["sku_text", "upc_text", "cost_number" ]}),
        ("Location", {"fields" : ["storage_number", "rack_number", "item_number"]}),

    ]
    list_display = ["title_text", "condition", "storage_number"]
    list_filter = ["condition"]
    search_fields = ["title_text"]
    inlines = [ImagesInLine]


    

admin.site.register(ProductInfo, ProductAdmin)