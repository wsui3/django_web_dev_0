from django import forms
from django.forms import extras
from .models import CarUser

class PictureForm(forms.Form):
	picture_text=forms.CharField(required=False)
	#picture_url=forms.CharField(required=False)
	picture_title=forms.CharField(required=False)
	picture=forms.ImageField(required=False)
	picture_owner=forms.CharField(required=False)

class CarUserForm(forms.Form):
	GENDER_CHOICES=(
		(u'Male',u'Male'),
		(u'Female',u'Female'),
	)
	gender=forms.ChoiceField(label='gender',choices=GENDER_CHOICES,widget=forms.RadioSelect())
	birthday=forms.DateField(required=False,label='birthday')
	self_introduce=forms.CharField(label='self_introduce',widget=forms.Textarea({'size':10000}))
	caruser=forms.CharField(required=False)
	# gender=forms.ChoiceField(required=False,choices=GENDER_CHOICES)
	# birthday=forms.DateField(required=False)
	# self_introduce=forms.CharField(required=False,widget=forms.Textarea)
	# caruser=forms.CharField(required=False)
	# class Meta:
	# 	model=CarUser
	# 	fields=('gender','self_introduce','birthday')