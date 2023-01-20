from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    address = models.TextField(max_length=500)
    buying_op = models.CharField(max_length=100)
    looking_for = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    display_picture = models.ImageField(upload_to='dp', blank=True, null=True)
    bg_picture = models.ImageField(upload_to='background', blank=True, null=True)
    contact_no = models.CharField(max_length=12)
    company_name = models.CharField(max_length=100)
    Materials = models.CharField(max_length=200)
    office_email = models.CharField(max_length=200)
    off_phone_no = models.CharField(max_length=12)
    
    
