from django_filters import rest_framework as filters
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema

from django_to_demo.serializer import DurationsSerializer
from django_to_demo.models import Durations


class DurationsListFilter(filters.FilterSet):
    client_id = filters.BaseCSVFilter(field_name='client_id', lookup_expr='in')


class DurationsList(generics.ListCreateAPIView):
    filterset_class = DurationsListFilter
    serializer_class = DurationsSerializer
    queryset = Durations.objects.all()
    #
    # @swagger_auto_schema(operation_description='Тестовый запрос к durations ')
    # def get(self, request, *args, **kwargs):
    #     return Durations.objects.filter(worker_id=self.kwargs['pk'])
