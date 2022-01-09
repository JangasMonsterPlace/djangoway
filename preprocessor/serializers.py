from rest_framework import serializers
from .models import CSV


class GenericCSVSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    class Meta:
        model = CSV
        fields = '__all__'