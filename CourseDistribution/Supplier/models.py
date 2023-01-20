from django.db import models

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
    
class BuyingOption(models.Model):
    opetion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.opetion
    
    
class LookingFor(models.Model):
    opetion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.opetion
    
    
class MaterialOptions(models.Model):
    opetion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.opetion