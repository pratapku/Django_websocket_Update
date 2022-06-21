from gen_apps.models import Message
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'







