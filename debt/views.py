from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


# Create your views here.
class CreateListLendersView(GenericAPIView):

  serializer_class = serializers.InputLenderSerializer

  def post(self, request):

    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      # serializer.validated_data['created_by'] = request.user
      serializer.save()

      return Response(data={
        'status': status.HTTP_201_CREATED,
        'message': "Lender created successfully",
        'data': serializer.data
      }, status=status.HTTP_201_CREATED)

    else: 
      return Response(data={
        'status': status.HTTP_400_BAD_REQUEST,
        'message': str(serializer.errors)
      }, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request):
    pass


class DetailUpdateDeleteLendersView(GenericAPIView):

  def patch(self, request, id):
    pass

  def get(self, request, id):
    pass

  def delete(self, request, id):
    pass


class CreateListDebtsView(GenericAPIView):
  
  serializer_class = serializers.InputDebtSerializer

  def post(self, request):
    pass

  def get(self, request):
    pass

class DetailUpdateDeleteDebtsView(GenericAPIView)

  def patch(self,request,id):
    pass

  def get(self,request,id):
    pass

  def delete(self, request, id):
    pass
