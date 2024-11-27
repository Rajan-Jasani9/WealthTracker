from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . models import Lender, Debt

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

    lenders = Lender.objects.all()
    serializer = serializers.ListDetailLenderSerializer(lenders, many=True)
    return Response(data={
      'status': status.HTTP_200_OK,
      'message': "Lenders retrieved successfully",
      'data': serializer.data
    }, status=status.HTTP_200_OK)

class DetailUpdateDeleteLendersView(GenericAPIView):

  def patch(self, request, id):
    lender = Lender.objects.filter(id=id).first()
    serializer = serializers.InputLenderSerializer(lender, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(data={
        'status': status.HTTP_200_OK,
        'message': "Lender updated successfully",
        'data': serializer.data
      }, status=status.HTTP_200_OK)
    else:
      return Response(data={
        'status': status.HTTP_400_BAD_REQUEST,
        'message': str(serializer.errors)
      }, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id):
    lender = Lender.objects.filter(id=id).first()
    serializer = serializers.ListDetailLenderSerializer(lender)

    return Response(data={
      'status': status.HTTP_200_OK,
      'message': "Lender retrieved successfully",
      'data': serializer.data
    }, status=status.HTTP_200_OK)

  def delete(self, request, id):
    lender = Lender.objects.filter(id=id).first()
    lender.is_delete=True
    lender.save()

    return Response(data={
      'status': status.HTTP_200_OK,
      'message': "Lender deleted successfully"
    }, status=status.HTTP_200_OK)


class CreateListDebtsView(GenericAPIView):
  
  serializer_class = serializers.InputDebtSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.validated_data['created_by'] = request.user
      serializer.validated_data
      serializer.save()

      return Response(data={
        'status': status.HTTP_201_CREATED,
        'message': "Debt created successfully",
        'data': serializer.data
      }, status=status.HTTP_201_CREATED)

  def get(self, request):
    debts = Debt.objects.all()
    serializer = serializers.ListDetailDebtSerializer(debts, many=True)
    return Response(data={
      'status': status.HTTP_200_OK,
      'message': "Debts retrieved successfully",
      'data': serializer.data
    }, status=status.HTTP_200_OK)

class DetailUpdateDeleteDebtsView(GenericAPIView):

  def patch(self,request,id):
    debt = Debt.objects.filter(id=id).first()
    serializer = serializers.InputDebtSerializer(debt, request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(data={
        'status': status.HTTP_200_OK,
        'message': "Debt updated successfully",
        'data': serializer.data
      }, status=status.HTTP_200_OK)
    else:
      return Response(data={
        'status': status.HTTP_400_BAD_REQUEST,
        'message': str(serializer.errors)
      }, status=status.HTTP_400_BAD_REQUEST)

  def get(self,request,id):
    debt = Debt.objects.filter(id=id).first()
    serializer = serializers.ListDetailDebtSerializer(debt)

    return Response(data={
      'status': status.HTTP_200_OK,
      'message': "Debt retrieved successfully",
      'data': serializer.data
    }, status=status.HTTP_200_OK)

  def delete(self, request, id):
    debt = Debt.objects.filter(id=id).first()
    debt.is_delete=True
    debt.save()
    return Response(data={
      'status': status.HTTP_200_OK,
      'message': "Debt deleted successfully"
    }, status=status.HTTP_200_OK)
