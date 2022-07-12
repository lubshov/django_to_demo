from django_to_demo.models import Durations
from rest_framework import serializers


class DurationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Durations
        fields = '__all__'
