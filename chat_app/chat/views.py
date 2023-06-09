from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return render(request, 'chat/home.html')

@login_required(login_url='login')
def room(request, room_name):
  #username = request.GET.get('username', 'Anonymous')
  username = request.user.username
  print('aaa'+username);
  messages = Message.objects.filter(room=room_name)[0:25]
  return render(request, 'chat/room.html', {'room_name': room_name, 'username': username,'messages': messages})



@login_required(login_url='login')
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/chat/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/chat/'+room+'/?username='+username)

@login_required(login_url='login')
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    print('username:'+username);
    print('room_id:'+username);
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')



def getMessagesApi(request, room_name):
    headers      = request.headers
    apikey       = request.headers.get('apikey')
    if(apikey=="test123"):

        messages = Message.objects.filter(room=room_name)
        return JsonResponse({"messages":list(messages.values())})
    else:
        return JsonResponse({"messages":'api key not valid'})



