import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import Image

# Create your models here.

class Picture(models.Model):
	picture_title=models.CharField(max_length=200)
	picture_text=models.CharField(max_length=10000)
	picture_owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	picture=models.ImageField(upload_to='polls/assets/',blank=True,null=True)
	pub_date=models.DateTimeField('date published')

	def __str__(self):
		return self.picture_title

	def was_published_recently(self):
		now=timezone.now()
		return now-datetime.timedelta(days=1)<=self.pub_date<=now
		was_published_recently.admin_order_field='pub_date'
		was_publiehed_recently.boolean=True
		was_published_recently.short_description='Published recently?'

class CarUser(models.Model):
	caruser = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	GENDER_CHOICES=(
		(u'M',u'Male'),
		(u'F',u'Female'),
	)
	gender=models.CharField(max_length=2,choices=GENDER_CHOICES)
	self_introduce=models.CharField(max_length=10000)
	birthday=models.DateField(null=True,max_length=20)