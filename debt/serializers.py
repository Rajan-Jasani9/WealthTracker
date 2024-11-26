from rest_framework import serializers
from .models import Lender, Debt


class InputLenderSerializer(serializers.ModelSerializer):

  class Meta:
    model = Lender
    fields = ['name', 'is_instituton', 'contact_number', 'email']


class ListDetailLenderSerializer(serializers.ModelSerializer):

  class Meta:
    model = Lender
    fields = ['name', 'is_institution', 'contact_number', 'email']


class InputDebtSerializer(serializers.ModelSerializer):

  class Meta:
    model = Debt
    fields = [
        'name', 'debt_type', 'principal_amount', 'interest_rate', 'start_date',
        'has_emis', 'emi_amount', 'total_installments', 'installments_paid',
        'due_date', 'status', 'currency', 'notes', 'lender'
    ]


class ListDetailDebtSerializer(serializers.ModelSerializer):

  lender = ListDetailLenderSerializer()

  class Meta:
    model = Debt
    fields = [
        'name', 'debt_type', 'principal_amount', 'interest_rate', 'start_date',
        'has_emis', 'emi_amount', 'total_installments', 'installments_paid',
        'due_date', 'status', 'currency', 'notes', 'lender'
    ]
