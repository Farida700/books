from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=10)
    genre = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    year = models.DateField(auto_created=True)
    date = models.DateField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    
    
