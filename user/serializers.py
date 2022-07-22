from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers a user profile object"""
    
    class Meta:
        model = UserProfileModel
        fields = ('id', 'phone', 'first_name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfileModel.objects.create_user(
            phone = validated_data['phone'],
            name = validated_data['first_name'],
            password = validated_data['password']
        )
        
        return user