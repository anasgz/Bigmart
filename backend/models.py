from django.db import models

# Create your models here.
class adminreg(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    EMAIL = models.CharField(max_length=50, null=True, blank=True)
    MOBILE = models.IntegerField(null=True, blank=True)
    USERNAME = models.CharField(max_length=50, null=True, blank=True)
    PASSWORD = models.CharField(max_length=50, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile")
class categorydb(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    DISCRIPTION = models.CharField(max_length=100, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile")

class productdb(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    PRICE = models.CharField(max_length=100, null=True, blank=True)
    QUANTITY = models.CharField(max_length=100, null=True, blank=True)
    DISCRIPTION = models.CharField(max_length=100, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile")
    CATEGORY = models.CharField(max_length=100, null=True, blank=True)

class contactdb(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    EMAIL = models.EmailField(max_length=100, null=True, blank=False)
    SUBJECT = models.CharField(max_length=100, null=True, blank=True)
    MESSAGE = models.CharField(max_length=100, null=True, blank=True)