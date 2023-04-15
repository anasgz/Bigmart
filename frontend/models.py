from django.db import models

# Create your models here.
class registrationdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Email=models.EmailField(max_length=30,null=True,blank=True)
    Password=models.CharField(max_length=30,null=True,blank=True)
    Conformpassword=models.CharField(max_length=30,null=True,blank=True)
