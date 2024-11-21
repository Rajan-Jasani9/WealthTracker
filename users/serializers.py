from rest_framework.serializers import ModelSerializer, Serializer
from .models import UserDetails
from rest_framework import serializers


class UserDetailSerializer(ModelSerializer):
  """
  Serializer to get user details.
  """

  class Meta:
    model = UserDetails
    fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ListUserSerializer(ModelSerializer):
  """
  Serializer for list of users.
  """ 
  class Meta:
      model = UserDetails
      fields = ['id', 'first_name', 'last_name']