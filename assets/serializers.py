from rest_framework import serializers
from .models import Asset

class AssetInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            'name',
            'description',
            'asset_type',
            'asset_status',
            'purchase_cost',
            'purchase_date',
            'value',
        ]

class AssetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            'id',
            'name',
            'asset_type',
            'asset_status',
            'purchase_date',
            'value',
        ]

class AssetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            'id',
            'name',
            'description',
            'asset_type',
            'asset_status',
            'purchase_cost',
            'purchase_date',
            'value',
            'created_at',
            'updated_at',
        ]
