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

class ProductInfo (models.Model):

    title_text = models.CharField ("Title" , max_length = 80)
    description_text = models.TextField ("Description", default = 'Insert a Description' ,max_length = 1000)
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
    
    #location #bodega y rack 

    def __str__(self):
        return self.title_text
    


