from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from .models import Asset


# Create your views here.
class CreateListAssetsView(GenericAPIView):

  def post(self, request):

    input_serializer = serializers.AssetInputSerializer(data=request.data)
    if input_serializer.is_valid():
      input_serializer.save()
      return Response(data={
          "status": status.HTTP_201_CREATED,
          "message": "Asset created successfully",
          "data": input_serializer.data,
      },
                      status=status.HTTP_201_CREATED)

    else:
      return Response(data={
          "status": status.HTTP_400_BAD_REQUEST,
          "message": "Invalid input",
      },
                      status=status.HTTP_400_BAD_REQUEST)

  def get(self, request):

    serializer = serializers.AssetListSerializer(Asset.objects.all(),
                                                 many=True)

    return Response(data={
        'status': status.HTTP_200_OK,
        'message': 'Assets retrieved successfully',
        'data': serializer.data,
    },
                    status=status.HTTP_200_OK)


class UpdateDetailDeleteAssetsView(GenericAPIView):

  def patch(self, request, id):

    asset = Asset.objects.get(id=id)
    if not asset:
      return Response(data={
          "status": status.HTTP_404_NOT_FOUND,
          "message": "Asset not found",
      },
                      status=status.HTTP_404_NOT_FOUND)

    input_serializer = serializers.AssetInputSerializer(asset,
                                                        data=request.data)
    if input_serializer.is_valid():
      input_serializer.save()
      return Response(data={
          "status": status.HTTP_200_OK,
          "message": "Asset updated successfully",
          "data": input_serializer.data,
      },
                      status=status.HTTP_200_OK)
    else:
        return Response(data={
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Invalid input",
        }, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id):
    asset = Asset.objects.get(id=id)
    if not asset:
      return Response(data={
          "status": status.HTTP_404_NOT_FOUND,
          "message": "Asset not found",
      },
                      status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.AssetDetailSerializer(asset)

    return Response(data={
        'status': status.HTTP_200_OK,
        'message': 'Asset retrieved successfully',
        'data': serializer.data,
    },
                    status=status.HTTP_200_OK)

  def delete(self, request, id):
    asset = Asset.objects.get(id=id)
    if not asset:
      return Response(data={
          "status": status.HTTP_404_NOT_FOUND,
          "message": "Asset not found",
      },
                      status=status.HTTP_404_NOT_FOUND)

    asset.delete()
    return Response(data={
        "status": status.HTTP_200_OK,
        "message": "Asset deleted successfully",
    },
                    status=status.HTTP_200_OK)
