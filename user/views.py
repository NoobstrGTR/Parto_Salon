from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, permissions 
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import UserProfileModel
from .serializers import UserProfileSerializer

from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_data(request):
    """Geting all of our user data from database chart"""
    user_data = UserProfileModel.objects.all()
    user_serializer = UserProfileSerializer(user_data, many=True)
    return Response(user_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_data_by_id(request, id):
    user_data_id = UserProfileModel.objects.filter(id=id)
    if not user_data_id:
        return Response('There is no user with that ID.', status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(user_serializer.data, status=status.HTTP_302_FOUND)


@api_view(['POST'])
@permission_classes([AllowAny])
def post_user_data(request):
    """Posting a new user to our database chart"""
    user_post_data = UserProfileSerializer(data=request.data)
    if user_post_data.is_valid():
        user_post_data.save()
        return Response(user_post_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response('didnt save it Error')



@api_view(['POST'])
@permission_classes([AllowAny])
def edit_user_data(request):
    """Edit the data by geting  a ID from FRONTEND"""
    edit_user_data = request.data
    find_user_data_in_database = UserProfileModel.objects.get(id=edit_user_data['id'])
    find_user_data_in_database.first_name = edit_user_data["first_name"]
    find_user_data_in_database.last_name = edit_user_data["last_name"]
    find_user_data_in_database.phone_number = edit_user_data["phone_number"]
    find_user_data_in_database.save()
    return Response('User successfully edited !', status=status.HTTP_200_OK)               


@api_view(['GET'])
@permission_classes([AllowAny])
def delete_user_data(request,id):
    delete_user_data = UserProfileModel.objects.filter(id=id)
    if not delete_user_data:
        return Response('user does not exist.', status=status.HTTP_404_NOT_FOUND)
    delete_user_data.delete()
    return Response('User deleted successfully', status=status.HTTP_410_GONE)


class  UserProfileViewSet(viewsets.ModelViewSet):
    """Handel createing and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfileModel.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('phone','first_name')
    
   
class UserLoginApiView(ObtainAuthToken):
    """Handel creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES