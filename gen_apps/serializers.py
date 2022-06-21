from attr import fields
from rest_framework import serializers

from .models import Message

class SerializerForm(serializers.ModelSerializer):
    class Meta:
        model = Message

        fields = '__all__'
