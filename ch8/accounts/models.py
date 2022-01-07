from django.db import models
from django.contrib.auth.models import AbstractUser
import math
from decimal import *
# Create your models here.

class CustomUser(AbstractUser):
	age = models.PositiveIntegerField(null= True, blank= True)
	height = models.DecimalField(null = True, max_digits = 4, decimal_places = 1)
	yearly_income = models.PositiveIntegerField(null = True, blank = True)
	penis_length = models.DecimalField(max_digits = 4,decimal_places = 2,null = True)

	@property
	def dq(self):
		total_q = 0
		age_q = 0
		height_q = 0
		income_q = 0
		penis_q = 0

		age_s = ''
		height_s = ''
		income_s = ''
		penis_s = ''

		if (self.age and self.height and self.yearly_income and self.penis_length):
			#age
			if self.age < 18:
				age_q = 0
				age_s = 'You are too young. '
			if self.age > 18 and self.age < 21 : 
				age_q = 1
				age_s = 'You are a bit too young. '
			if self.age > 21 and self.age < 30:
				age_q = 2
				age_s = 'You are within a good age range. '
			if self.age > 30 and self.age < 40:
				age_q = 1
				age_s = 'You are a bit too old. '
			if self.age > 40 :
				age_q = 0
				age_s = 'You are too old. '

			#height
			if self.height < 60:
				height_q = -2
				height_s = "You are way too short. "
			elif self.height < 65:
				height_q = -1
				height_s = "You are too short. "
			elif self.height < 68:
				height_q = 0
				height_s = "You are a bit too short. "
			elif self.height < 70:
				height_q = 1
				height_s = "You are a good height. "
			elif self.height < 72:
				height_q = 2
				height_s = "You are a good height. "
			elif self.height < 74:
				height_q = 4
				height_s = "You are tall. "
			elif self.height < 76:
				height_q = 3
				height_s = "You are a bit too tall. "
			elif self.height > 76:
				height_q = 1
				height_s = "You are way too tall. "
			#income
			if self.yearly_income < 35000:
				income_q = -1
				income_s = "You are way too poor. "
			elif self.yearly_income < 50000:
				income_q = 0
				income_s = "You are  too poor. "
			elif self.yearly_income <70000:
				income_q = 0.5
				income_s = "You are a bit too poor. "
			elif self.yearly_income <90000:
				income_q = 1
				income_s = "You make an alright salary. "
			elif self.yearly_income <100000:
				income_q = 1.5
				income_s = "You make a decent salary. "
			elif self.yearly_income <120000:
				income_q = 2
				income_s = "You make a good salary. "
			elif self.yearly_income < 150000:
				income_q = 2.5
				income_s = "You make a great salary! "
			elif self.yearly_income <200000:
				income_q = 3
				income_s = "You make a really great salary! "
			elif self.yearly_income >200000:
				income_q = 4
				income_s = "You make fucking bands!!! "
			#penis
			if self.penis_length < 2:
				penis_q = -1
				penis_s = "Your dick is too small. "
			elif self.penis_length <4:
				penis_q = 0
				penis_s = "Your dick is small. "
			elif self.penis_length <5:
				penis_q = 0.5
				penis_s = "Your dick is ok. "
			elif self.penis_length <6:
				penis_q = 1
				penis_s = "Your dick good. "
			elif self.penis_length <7:
				penis_q = 2
				penis_s = "Your dick is great! "
			elif self.penis_length <9:
				penis_q = 2.5
				penis_s = "Your dick is HUGE! "
			elif self.penis_length >9:
				penis_q = 0
				penis_s = "Your dick is too big. "


			total_q = age_q + income_q + height_q + penis_q
			if total_q > 10:
				total_q = 10
			elif total_q < 0:
				total_q = 0


			return age_s + height_s + income_s + penis_s + "Your Desirability Score is: " +str(total_q) +"/10! "

		else:
			return ""