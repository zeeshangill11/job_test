from django.urls import path,include
from django.urls import path
from account2 import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from django.contrib import admin

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.account_login, name='login'),
    path('account/', include('account2.urls')),
    path('posts/', include('posts.urls')),
    path('chat/', include('chat.urls')),
    
    path('logout/', views.logout_view, name='logout'),

    # Add more URL patterns as needed
] 