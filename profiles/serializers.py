from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model
from .models import Profile
                                    
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """ User serializer """
    class Meta:
        model = User
        fields = ['username',]

class ProfileSerializer(serializers.ModelSerializer):
    """ Profile user serializer """
    user = UserSerializer()

    class Meta:
        model = Profile
        exclude = ['created', 'updated']
        #fields ='__all__'

class MinProfileSerializer(serializers.ModelSerializer):
    """ Profile mini serializer """
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'photo']
