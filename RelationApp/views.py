from sre_parse import CATEGORIES
from django.shortcuts import render
from .models import *


# Create your views here.

def relation(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories' :categories,
        'products':products
        
    }
    return render(request,'RelationApp\Relation.html',context)

def category(request,name):
    categories = Category.objects.get(name = name)
    products = Product.objects.filter(category=categories)
    context = {
        'categories' :categories,
        'products':products
        
    }
    
    return render(request,'RelationApp\category.html',context)