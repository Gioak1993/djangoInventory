from django.db import models

# Create your models here.

''' lets create a product model here, it should have the following

-Title
-Description
-image
-sku
-upc
-Measurements (inches)
-Weight (pounds) 
-Cost
-Price




'''

class Category(models.Model):
    name_text = models.CharField("Category Name", max_length= 75)

    def __str__(self):
        return self.name_text

class ProductInfo (models.Model):

    title_text = models.CharField ("Title" , max_length = 200)
    description_text = models.TextField ("Description", max_length = 5000)
    sku_text = models.CharField ("SKU", default = 'noSku', max_length = 20)
    upc_text = models.CharField ("UPC", default = 'noUpc', max_length = 15)
    cost_number = models.FloatField ("Cost", default = 0)
    price_number = models.FloatField ("Price", default = 0)
    CONDITIONS = {
        "BN" : "Brand New",
        "LN" : "Like New",
        "AC" : "Acceptable",
        "DA" : "Damage",
        "MP" : "Missing Parts",
    }
    condition = models.CharField ("Condition", default = "LN",max_length = 20, choices = CONDITIONS)
    storage_number = models.IntegerField("Storage Number", default = 0)
    rack_number = models.IntegerField("Rack number",default = 0)
    item_number = models.IntegerField("Item number", default = 0)
    show_onstore = models.BooleanField("Show in store?",default = True)
    quantity = models.IntegerField("Quatity",default = 0)
    category = models.ManyToManyField(Category)
    


    #location #bodega y rack 

    def __str__(self):
        return self.title_text
    


class Images(models.Model):
    image_url = models.ImageField()
    alt_text = models.CharField(max_length=255)
    onProduct = models.ForeignKey(ProductInfo, related_name = "images", on_delete= models.CASCADE)

