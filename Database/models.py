from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
   state_choices = (
   	('Andra Pradesh', 'Andra Pradesh'),
   	(' Arunachal Pradesh', 'Arunachal Pradesh'),
   	('Assam', 'Assam'),
   	('Bihar', 'Bihar'),
   	('Chhattisgarh', 'Chhattisgarh'),
   	('Goa', 'Goa'),
  	('Gujarat', 'Gujarat'),
   	('Haryana', 'Haryana'),
   	('Himachal Pradesh', 'Himachal Pradesh'),
   	('Jammu & Kashmir', 'Jammu & Kashmir'),
   	('Jharkhand', 'Jharkhand'),
   	('Karnataka', 'Karnataka'),
   	('Kerala', 'Kerala'),
   	('Madhya Pradesh', 'Madhya Pradesh'),
   	('Maharashtra', 'Maharashtra'),
   	('Manipur', 'Manipur'),
   	('Meghalaya', 'Meghalaya'),
   	('Mizoram', 'Mizoram'),
   	('Nagaland', 'Nagaland'),
   	('Odisha', 'Odisha'),
   	('Punjab', 'Punjab'),
   	('Rajasthan', 'Rajasthan'),
   	('Sikkim', 'Sikkim'),
   	('Tamil Nadu', 'Tamil Nadu'),
   	('Telangana', 'Telangana'),
   	('Tripura', 'Tripura'),
   	('Uttarakhand', 'Uttarakhand'),
   	('Uttar Pradesh', 'Uttar Pradesh'),
   	('West Bengal', 'West Bengal'),
   )
   name = models.CharField(max_length = 25)
   state = models.CharField(max_length =25 ,choices=state_choices)
   club = models.CharField(max_length = 50)
   sex_choice = (
   	('Male', 'Male'),
   	('Female', 'Female'),
   )
   sex = models.CharField(max_length =6, choices=sex_choice)
   dob = models.DateField()
   weight = models.IntegerField()
   age = models.IntegerField(default=0)
   category = models.CharField(max_length = 100,default='Auto Generated')
   
   def __unicode__ (self):
     	return unicode(self.id)
   def __str__ (self):
     	return unicode(self.id)
     	
     	
class Referee(models.Model):
   state_choices = (
   	('Andra Pradesh', 'Andra Pradesh'),
   	(' Arunachal Pradesh', 'Arunachal Pradesh'),
   	('Assam', 'Assam'),
   	('Bihar', 'Bihar'),
   	('Chhattisgarh', 'Chhattisgarh'),
   	('Goa', 'Goa'),
  	('Gujarat', 'Gujarat'),
   	('Haryana', 'Haryana'),
   	('Himachal Pradesh', 'Himachal Pradesh'),
   	('Jammu & Kashmir', 'Jammu & Kashmir'),
   	('Jharkhand', 'Jharkhand'),
   	('Karnataka', 'Karnataka'),
   	('Kerala', 'Kerala'),
   	('Madhya Pradesh', 'Madhya Pradesh'),
   	('Maharashtra', 'Maharashtra'),
   	('Manipur', 'Manipur'),
   	('Meghalaya', 'Meghalaya'),
   	('Mizoram', 'Mizoram'),
   	('Nagaland', 'Nagaland'),
   	('Odisha', 'Odisha'),
   	('Punjab', 'Punjab'),
   	('Rajasthan', 'Rajasthan'),
   	('Sikkim', 'Sikkim'),
   	('Tamil Nadu', 'Tamil Nadu'),
   	('Telangana', 'Telangana'),
   	('Tripura', 'Tripura'),
   	('Uttarakhand', 'Uttarakhand'),
   	('Uttar Pradesh', 'Uttar Pradesh'),
   	('West Bengal', 'West Bengal'),
   )
   name = models.CharField(max_length = 25)
   state = models.CharField(max_length =25 ,choices=state_choices)
   phone = models.IntegerField()
   def __unicode__ (self):
     	return unicode(self.name)
   def __str__ (self):
     	return unicode(self.name)

