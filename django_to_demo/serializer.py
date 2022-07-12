from django_to_demo.models import Durations, Clients, Equipment, Modes
from rest_framework import serializers


class DurationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Durations
        fields = '__all__'

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class ModesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modes
        fields = '__all__'


# class DurationsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Durations
#         fields = '__all__'
