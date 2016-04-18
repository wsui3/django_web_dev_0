from django.contrib import admin

#from .models import Question,Choice
from .models import Picture,CarUser
from django.contrib.auth.models import User

# Register your models here.

class PictureInline(admin.TabularInline):
	model=Picture
	extra=3
	
class PictureAdmin(admin.ModelAdmin):
	fieldsets=[(None,{'fields':['picture_title']}),(None,{'fields':['picture_text']}),('Date information',{'fields':['pub_date']}),]
	#inlines=[PictureInline]
	list_display=('picture_title','pub_date','was_published_recently')
	list_filter=['pub_date']
	search_fields=['picture_text']

admin.site.register(Picture)

class CarUserInline(admin.TabularInline):
	model=CarUser
	extra=3

class CarUserAdmin(admin.ModelAdmin):
	fieldsets=[
		(None,{'fields':['gender']}),
		(None,{'fields':['self_introduce']}),
		(None,{'fields':['birthday']}),
	
	]

admin.site.register(CarUser)