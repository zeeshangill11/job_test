from django.urls import path
from . import views
app_name='chat'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room_name>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    #path('getMessages/<str:room_name>/', views.getMessages, name='getMessages'),
    path('api/get_messages/<str:room_name>/', views.getMessagesApi, name='get_messages_api'),

]