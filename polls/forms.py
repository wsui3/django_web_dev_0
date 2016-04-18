from django import forms
#from django.forms import extras

class PictureForm(forms.Form):
	picture_text=forms.CharField(required=False)
	#picture_url=forms.CharField(required=False)
	picture_title=forms.CharField(required=False)
	picture=forms.ImageField(required=False)
	picture_owner=forms.CharField(required=False)

class CarUserForm(forms.Form):
	GENDER_CHOICES=(
		(u'M',u'Male'),
		(u'F',u'Female'),
	)
	# gender=forms.ChoiceField(label=u'gender',choices=GENDER_CHOICES,widget=forms.RadioSelect())
	# birthday=forms.DateField(required=False,widget=extras.SelectDateWidget(years=range(1800,2020)),label='birthday')
	# self_introduce=forms.CharField(label=u'self_introduce',widget=forms.Textarea({'size':10000}))
	# caruser=forms.CharField(required=False)
	gender=forms.ChoiceField(required=False)
	birthday=forms.DateField(required=False)
	self_introduce=forms.CharField(required=False)
	caruser=forms.CharField(required=False)