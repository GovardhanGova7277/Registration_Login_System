from django.db import models

# Create your models here.

class People(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    phone = models.BigIntegerField(unique = True)
    email = models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 30)
    hobbies = models.CharField(max_length = 100)
    country = models.CharField(max_length = 30)
    
    

