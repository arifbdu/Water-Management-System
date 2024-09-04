from rest_framework import serializers
from .models import CustomUser, PondData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PondDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PondData
        fields = '__all__'
