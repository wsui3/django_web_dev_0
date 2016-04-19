from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse, FileResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Picture,CarUser
from .forms import PictureForm,CarUserForm
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.template import RequestContext,Context,Template

# Create your views here.
def index(request):
	return render(request,'polls/index.html')

def list_view(request):
	# test comments
	Picture.picture_owner=request.user
	current_user_id=request.user.id
	picture=Picture.objects.all()
	latest_picture_list=Picture.objects.filter(picture_owner_id=current_user_id).order_by('-pub_date')
	lst = []
	for i in latest_picture_list:
		if i.picture:
			lst.append(i)

	context={'latest_picture_list': lst}
	return render(request,'polls/list.html',context)

def login_user(request):
	context={'csrf_token':request}
	return render(request,'polls/login.html')

def auth(request):
	#username=request.POST.get('username','')
	#password=request.POST.get('password','')
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(username=username,password=password)
	if user is not None:
		if user.is_active:
			login(request,user)
			return HttpResponseRedirect('list')
		else:
			return False
	else:
		return HttpResponseRedirect('invalid')

def invalid(request):
	return render(request,'polls/invalid.html')

def logout_view(request):
	logout(request)
	return render(request,'polls/index.html')

@login_required(login_url='/polls/login/')
def upload(request):
	return render(request,'polls/upload.html')

@require_POST
def upload_image(request):
	form = PictureForm(request.POST, request.FILES)
	Picture.picture_owner=request.user
	current_user_id=request.user.id
	if form.is_valid():
		picturetitle = form.cleaned_data['picture_title']
		picturetext = form.cleaned_data['picture_text']
	if 'picfile' in request.FILES:
		image = request.FILES['picfile']
	else:
		image = None
	s = Picture(
		pub_date = timezone.now(),
		picture = image,
		picture_owner_id = current_user_id,
		picture_title = picturetitle,
		picture_text = picturetext)
	s.save()
	return HttpResponse("OK")

def get_image_temp(request):
	lst = Picture.objects.all()
	for i in lst:
		print i.picture.url if i.picture else "picture empty"
	return HttpResponse("OK")

def get_media_file(request, file_path):
	import os
	from django.conf import settings
	full_path = os.path.join(settings.MEDIA_ROOT, 'polls/assets/', file_path)
	return FileResponse(open(full_path, 'rb'))

#show user center
@login_required(login_url='/polls/login/')
def user_center(request):
	CarUser.caruser=request.user
	current_user_id=request.user.id
	current_caruser_list=CarUser.objects.filter(caruser_id=current_user_id)
	caruser=CarUser.objects.all()
	context={'current_caruser_list':current_caruser_list}

	return render(request,'polls/user_center.html',context)

#create caruser
@login_required(login_url='/polls/login/')
def edit_caruser(request):
	CarUser.caruser=request.user
	current_user_id=request.user.id
	current_caruser_list=CarUser.objects.filter(caruser_id=current_user_id)
	caruser=CarUser.objects.all()
	context={'current_caruser_list':current_caruser_list}
	return render(request,'polls/edit_caruser.html',context)

@require_POST
def update_caruser(request):
	form=CarUserForm(request.POST)#form include the data we have submited.
	CarUser.caruser=request.user
	current_user_id=request.user.id
	current_caruser_list=CarUser.objects.filter(caruser_id=current_user_id)
	if form.is_valid():#if the data is legal.
		gender=form.cleaned_data['gender']
		birthday=form.cleaned_data['birthday']
		self_introduce=form.cleaned_data['self_introduce']
		s=CarUser(
			gender=gender,
			birthday=birthday,
			#caruser_id=current_user_id,
			self_introduce=self_introduce)
		s.save()
		return HttpResponse("OK")
	else:
		#print form.error.as_json()
		return HttpResponse("Something wrong with the form")
		# form=CarUserForm()
	# args={}
	# args.update(request)

	# args['form']=form