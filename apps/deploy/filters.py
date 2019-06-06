__author__ = 'singo'
__datetime__ = '2019/4/28 11:11 AM '


from django_filters import ChoiceFilter, CharFilter, rest_framework, IsoDateTimeFilter
from django.db import models as django_models

from .models import DeploymentOrder, ENV, STATUS, TYPE, History, HISTORY_STATUS


class DeploymentOrderFilter(rest_framework.FilterSet):
    '''
    上线单过滤
    '''

    project = CharFilter(field_name='project__name', lookup_expr='icontains')
    env = ChoiceFilter(choices=ENV)
    status = ChoiceFilter(choices=STATUS)
    type = ChoiceFilter(choices=TYPE)
    applicant = CharFilter(field_name='applicant__name', lookup_expr='icontains')
    reviewer = CharFilter(field_name='reviewer__name', lookup_expr='icontains')
    assign_to = CharFilter(field_name='assign_to__name', lookup_expr='icontains')

    class Meta:
        model = DeploymentOrder
        fields = ['project', 'env', 'status', 'type', 'applicant', 'reviewer', 'assign_to']


class DeployHistoryFilter(rest_framework.FilterSet):
    project_name = CharFilter(lookup_expr='icontains')
    env = ChoiceFilter(choices=ENV)
    result = ChoiceFilter(choices=HISTORY_STATUS)
    type = ChoiceFilter(choices=TYPE)

    applicant = CharFilter(lookup_expr='icontains')
    reviewer = CharFilter(lookup_expr='icontains')
    assign_to = CharFilter(lookup_expr='icontains')


    class Meta:
        model = History
        # fields = ['project_name', 'env', 'result', 'type', 'applicant', 'reviewer', 'assign_to', 'end']
        fields = {
            'end': ('lte', 'gte')
        }

        filter_overrides = {
            django_models.DateTimeField: {
                'filter_class': IsoDateTimeFilter
            },
        }
