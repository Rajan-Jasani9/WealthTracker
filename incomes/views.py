from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . models import Income

# Create your views here.
class CreateListIncomesView(GenericAPIView):

     def post(self, request):
          pass

     def get(self, request):
          pass

class DetailUpdateDeleteIncomesView(GenericAPIView):

     def get(self, request, id):
          pass

     def patch(self, request, id):
          pass