from rest_framework.response import Response
from rest_framework import status, permissions 
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import *
from .serializers import *

@api_view(['GET'])
@permission_classes([AllowAny])
def get_description_data(request):
    """Geting all of our user data from database chart"""
    description_data = DescriptionModel.objects.all()
    description_serializer = DescriptionSerializer(data=description_data, many=True)
    return Response(description_serializer.data, status=status.HTTP_200_OK)

