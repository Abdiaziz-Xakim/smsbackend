# fees_app/serializers.py
from rest_framework import serializers
from .models import  Feepayment

class FeePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feepayment
        fields = ['id', 'regno', 'fullname','payment_date', 'amount']
