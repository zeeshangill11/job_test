from django.urls import path, re_path
from posts import views
from django.contrib.auth.decorators import login_required
app_name = 'posts'
urlpatterns = [
    re_path(r'^list/', views.post_list, name='post_list'),
    re_path(r'^add/', views.add_post, name='add_post'),

    path('<int:pk>/delete/', views.delete_post, name='delete_post'),


]
