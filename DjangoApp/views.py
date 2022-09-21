from contextlib import _RedirectStream, redirect_stdout
from django.shortcuts import redirect
from django.shortcuts import render
from .models import post

# Create your views here.



def app(request):
    
    posts = post.objects.all().filter(is_published=True).order_by('-created_dt')
    context = {
        'posts':posts, 
    }
    
    return render(request,'DjangoApp\index.html',context)


