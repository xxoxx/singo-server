__author__ = 'singo'
__datetime__ = '2019/4/28 11:11 AM '


from django_filters import ChoiceFilter, CharFilter, rest_framework, IsoDateTimeFilter
from django.db import models as django_models

from .models import DeploymentOrder, ENV, STATUS, TYPE, History, HISTORY_STATUS, DeployEnv, DeployItem


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


class DeployItemFilter(rest_framework.FilterSet):
    # parents = DeployEnv.objects.filter(parent=None)
    parent =  CharFilter(field_name='sub_env__parent__name', label='parent env name')
    name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = DeployItem
        fields = ['parent']


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
