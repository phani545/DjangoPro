from datetime import datetime
from django.db import models


# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=120)
    description=models.TextField()
    img = models.ImageField(upload_to='photos/',max_length=100)
    vediofile =models.FileField(upload_to='vedio/', max_length=100)
    author=models.CharField(max_length=50)
    created_dt=models.DateField(default=datetime.now,blank=True)
    is_published=models.BooleanField(default=False)
        

    class Meta:
        verbose_name = ("post")
        verbose_name_plural = ("posts")
        
        
    def __str__(self):
        return self.title


  

