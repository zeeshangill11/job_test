from django.urls import re_path,path
from . import views

app_name='account2'
urlpatterns = [
  
    re_path(r'^login/$', views.login_view,name='account_login'),
	
	re_path(r'^account_signup/', views.signup_view,name='account_signup'),
	re_path(r'^logout/', views.logout_view,name='logout'),    
]
