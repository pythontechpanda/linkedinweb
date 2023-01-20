from django.db import models
# from accounts.models import User
# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=200)
    
    def __str__(self):
        return self.country
    
class State(models.Model):
    state = models.CharField(max_length=200)
    con_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.state
    
    
class City(models.Model):
    city = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.city
    
class Qualification(models.Model):
    opetion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.opetion
    
    
class LookingFor(models.Model):
    opetion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.opetion
    
    
class CoursesOptions(models.Model):
    opetion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.opetion
    
    
class CompanyProfile(models.Model):
    name = models.CharField(max_length=200)
    display_picture = models.ImageField(upload_to='dp', blank=True, null=True)
    bg_picture = models.ImageField(upload_to='background', blank=True, null=True)
    email = models.CharField(max_length=200)
    service = models.CharField(max_length=300)
    discription = models.CharField(max_length=1000)
    contact = models.CharField(max_length=12)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name