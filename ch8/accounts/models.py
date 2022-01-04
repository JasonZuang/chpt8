from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	age = models.PositiveIntegerField(null= True, blank= True)
	height = models.DecimalField(null = True, max_digits = 4, decimal_places = 1)
	yearly_income = models.PositiveIntegerField(null = True, blank = True)
	penis_length = models.DecimalField(max_digits = 4,decimal_places = 2,null = True)