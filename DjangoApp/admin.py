from django.contrib import admin
from .models import post
# Register your models here.

class postadmin(admin.ModelAdmin):
    list_display = ('id','title','description','author','created_dt','is_published')
    list_display_links = ('title',)
    list_filter = ('title','created_dt','is_published')

admin.site.register(post,postadmin)