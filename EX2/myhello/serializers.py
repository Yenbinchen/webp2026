from rest_framework import serializers
from .models import MyHello

class MyHelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyHello
        fields = '__all__'