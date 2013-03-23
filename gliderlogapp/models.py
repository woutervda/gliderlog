from django.db import models
from django import forms
from django.forms import ModelForm
import datetime

class Registration(models.Model):
	flightnumber = models.IntegerField(null=True, blank=True)
	start_method = models.CharField(max_length=200)
	glider_registration = models.CharField(max_length=10)
	captain = models.CharField(max_length=200)
	passenger = models.CharField(max_length=200,null=True, blank=True)
	start_time = models.DateTimeField()
	landing_time = models.DateTimeField(null=True, blank=True)
	# length = models.IntegerField()
	def length_auto(self, null=True, blank=True):
		if self.landing_time != None:
			return self.landing_time - self.start_time
		else:
			return 0
	remarks = models.CharField(max_length=500, null=True, blank=True)
	def __unicode__(self):
		return self.start_method
		return self.glider_registration
		return self.captain
		return self.passenger
		return self.remarks
		
STARTMETHODS = (
	('Lier', 'Lierstart'),
	('Sleep', 'Sleepstart'),
	('Zelf', 'Zelfstart'),
	)
	
class EntryForm(forms.Form):
	flightnumber = forms.IntegerField(required=False)
	start_method = forms.ChoiceField(choices=STARTMETHODS)
	glider_registration = forms.CharField()
	captain = forms.CharField()
	passenger = forms.CharField(required=False)
	start_time = forms.DateTimeField(required=False)
	landing_time = forms.DateTimeField(required=False)
	remarks = forms.CharField(required=False)
	
# class EntryForm(ModelForm):
	# class Meta:
		# model = Registration
		
class Officials(models.Model):
	DDI_morning = models.CharField(max_length=200, null=True, blank=True)
	DDI_afternoon = models.CharField(max_length=200, null=True, blank=True)
	StartOfficer_morning = models.CharField(max_length=200, null=True, blank=True)
	StartOfficer_afternoon = models.CharField(max_length=200, null=True, blank=True)
	Date = models.DateTimeField()
