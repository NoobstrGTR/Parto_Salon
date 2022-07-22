from rest_framework import serializers
from .models import *


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesModel
        fields = "__all__"
        
class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionModel
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'date', 'start_time', 'end_time')