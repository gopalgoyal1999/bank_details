from rest_framework import serializers
from .models import Bank

class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Bank
        fields = ("branch","ifsc")

class BankListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Bank
        fields = ("bank_name","city")


