from django.db import models  
 
class Product(models.Model):  
    pid = models.IntegerField(unique=True, error_messages ={
                    "unique":"Please enter a unique product Id."
                    },
                    blank=False,null=False)  
    pname = models.CharField(max_length=100)  
    pdescription = models.CharField(max_length=200) 
    pqty = models.IntegerField(blank=False,null=False, default=10) 
    price = models.IntegerField(blank=False,null=False, default=100) 
    class Meta:  
        db_table = "product"  
