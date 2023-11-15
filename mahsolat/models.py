from django.db import models


class kala(models.Model):
    name=models.CharField(max_length=50)
    price=models.TextField(max_length=50)
    details=models.TextField()
    img=models.ImageField(upload_to="aks")
    
class contact(models.Model):
   
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    onvan=models.CharField(max_length=150)
    text=models.CharField(max_length=500)
    number=models.CharField(max_length=11,default='09130000000')