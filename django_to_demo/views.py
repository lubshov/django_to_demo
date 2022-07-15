from django_filters import rest_framework as filters
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render
from django_to_demo.serializer import DurationsSerializer, ClientsSerializer, EquipmentSerializer, ModesSerializer
from django_to_demo.models import Durations, Clients, Equipment, Modes
from django.http import HttpResponse
import django_filters


class DurationsListFilter(filters.FilterSet):
    client = filters.BaseCSVFilter(field_name='client_id', lookup_expr='in')
    equipment = filters.BaseCSVFilter(field_name='equipment_id', lookup_expr='in')
    modes = filters.BaseCSVFilter(field_name='mode_id', lookup_expr='in')


class ClientsListFilter(filters.FilterSet):
    client = filters.BaseCSVFilter(field_name='id', lookup_expr='in')


class DurationsList(generics.ListCreateAPIView):
    filterset_class = DurationsListFilter
    serializer_class = DurationsSerializer
    queryset = Durations.objects.all()


class ClientsList(generics.ListCreateAPIView):
    filterset_class = ClientsListFilter
    serializer_class = ClientsSerializer
    queryset = Clients.objects.all()


class EquipmentList(generics.ListCreateAPIView):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()


class ModesList(generics.ListCreateAPIView):
    serializer_class = ModesSerializer
    queryset = Modes.objects.all()


def index(request):
    clients = Clients.objects.all()
    modes = Modes.objects.all()
    equipments = Equipment.objects.all()
    return render(request, 'django_to_demo/index.html', locals())
