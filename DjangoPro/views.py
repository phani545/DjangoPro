from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

#def home(request):
 #   return HttpResponse('<h1> Hello, This is Phani Deep Challa </h1>')
 
 
 
def home(request):
    name = 'Phani Deep Challa'
    age = 33
    colors = ['red','yellow','blue']
    return render(request,'index.html',{'name':name,'age':age,'colors':colors})
      
def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})
