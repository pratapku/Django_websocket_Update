from django.shortcuts import render,HttpResponse
from .models import Message
from .serializers import SerializerForm
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView





class ListRead(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = SerializerForm

class RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = SerializerForm




def index(request):
    return HttpResponse('hello pratap')

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})
