from django.contrib import admin
from .models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','product_name','created_date')
    list_display_links = ('product_name',)
    list_filter = ('category','created_date')
    list_editable = ('category',)
    list_per_page = 1
    #readonly_fields = ('product_name')
   
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)