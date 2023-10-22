from rest_framework import serializers
from .models import IndianState

class IndianStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndianState
        fields = '__all__'