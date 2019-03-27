from rest_framework import generics
import django_filters
from .models import WorkOrder


class WorkOrderFilter(django_filters.rest_framework.FilterSet):
    '''
    工单过滤
    '''
    class Meta:
        model = WorkOrder
        fields = ['type', 'status']

