from gen_apps.models import Message
from gen_apps.api.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework .permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListCreateAPIView
class UserViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ListRead(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = UserSerializer
