import datetime

from rest_framework import serializers
from gtaapi.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    password=serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    status = serializers.BooleanField(default=True)

    def create(self,validated_data):
        print(validated_data)
        return User.objects.create(**validated_data)

    def update(self,instance,validated_data):
        if validated_data.get('name',instance.name):
            instance.name=validated_data.get('name',instance.name)
        if validated_data.get('email',instance.email):
             instance.email=validated_data.get('email',instance.email)
        if validated_data.get('password',instance.password):
            instance.password=validated_data.get('password',instance.password)
        instance.updated_at=datetime.datetime.today()
        instance.save()
        return instance


