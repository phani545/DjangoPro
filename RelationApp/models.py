from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,default = 'uncategorized')
    is_active = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'categories')
    product_name = models.CharField(max_length=50)      
    desc = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
       
   
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
   
    def __str__(self):
        return self.product_name
 
   
