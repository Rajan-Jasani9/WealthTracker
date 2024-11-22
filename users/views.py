from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import UserDetails, UserToken
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password, make_password
# from django.utils import timezone
from datetime import datetime, timedelta, timezone
import jwt, json, string, random
from . import serializers
from django_project import settings
from .utils import UserTokenAuthentication


# Create your views here.
class UserListView(GenericAPIView):

    authentication_classes = [UserTokenAuthentication]
    serializer_class = serializers.UserDetailSerializer

    def get(self, request):
        serializer = self.get_serializer(request.user)

        return Response(data={
            'status': status.HTTP_200_OK,
            'message': "User Details",
            'data': serializer.data
        },
                        status=status.HTTP_200_OK)


class LoginView(GenericAPIView):

    def post(self, request):

        username = request.data['username']
        password = request.data['password']

        user = UserDetails.objects.filter(username=username).first()

        if not user:
            return Response(data={
                'status': status.HTTP_400_BAD_REQUEST,
                'message': "Invalid Credentials"
            },
                            status=status.HTTP_400_BAD_REQUEST)

        else:
            is_correct_password = check_password(password, user.password)
            # password hash
            if not is_correct_password:
                return Response(data={
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': "Invalid Credentials"
                },
                                status=status.HTTP_400_BAD_REQUEST)

            if not user.is_active:
                return Response(data={
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': "User is not active"
                },
                                status=status.HTTP_400_BAD_REQUEST)

            # token generate
            dt = datetime.now(tz=timezone.utc) + timedelta(days=100)
            letters = string.ascii_letters
            random_string = ''.join(random.choice(letters) for i in range(15))
            payload = {
                'exp': dt,
                'id': user.id,
                'email': user.email,
                'random_string': random_string
            }
            encoded_token = jwt.encode(payload,
                                       settings.SECRET_KEY,
                                       algorithm='HS256')
            # token generate

            UserToken.objects.create(user=user, token=encoded_token)

            serializer = serializers.UserDetailSerializer(user)

            return Response(data={
                "status": status.HTTP_200_OK,
                "detail": "User successfully login, Token Generated.",
                "data": {
                    'token': encoded_token,
                    'user_data': serializer.data
                }
            },
                            status=status.HTTP_200_OK)
