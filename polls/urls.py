from django.conf.urls import url

from . import views
from django.conf import settings

app_name='polls'
urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^list/$',views.list_view,name='list_view'),
	url(r'^accounts/list/$',views.list_view,name='list_view'),
	url(r'^login/$',views.login_user,name='login'),
	url(r'^user/$',views.user_center,name='user_center'),
	url(r'^edit/$',views.edit_caruser,name='edit_caruser'),
	url(r'^update_caruser',views.update_caruser,name='update_caruser'),

	url(r'^accounts/$',views.auth,name='auth'),
	url(r'^accounts/index/$',views.index,name='auth_index'),
	#url(r'^auth/loggedin/$',views.loggedin,name='loggedin'),
	url(r'^accounts/logout/$',views.logout_view,name='logout'),
	url(r'^accounts/invalid/$',views.invalid,name='invalid'),
	url(r'^upload/$',views.upload,name='upload'),
	url(r'^upload_image', views.upload_image),
	url(r'^tmp', views.get_image_temp),
	url(r'^assets/(?P<file_path>.*)/', views.get_media_file),
]