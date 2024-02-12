from django.contrib import admin
from .models import ProductInfo, Images, Category

# Register your models here.

class ImagesInLine(admin.StackedInline):
    model = Images
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title_text", "description_text", "condition", "price_number"]}),
        ("Item Specifics", {"fields": ["sku_text", "upc_text", "cost_number", "category"]}),
        ("Location", {"fields" : ["storage_number", "rack_number", "item_number"]}),
        ("Sold and Show In Store", {"fields": ["show_onStore", "sold"]})

    ]
    list_display = ["title_text", "condition", "storage_number"]
    list_filter = ["condition", "sold" ]
    search_fields = ["title_text"]
    inlines = [ImagesInLine]


    

admin.site.register(ProductInfo, ProductAdmin)
admin.site.register(Category)
