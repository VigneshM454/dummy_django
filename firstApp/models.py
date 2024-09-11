from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    category=models.CharField(max_length=100)
    s_desc=models.CharField(max_length=100)
    l_desc=models.CharField(max_length=500)
    #image=models.ImageField(upload_to='uploadedImages/')
    
    def __str__(self):
        return self.name