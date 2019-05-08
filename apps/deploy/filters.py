__author__ = 'singo'
__datetime__ = '2019/4/28 11:11 AM '


import django_filters

from .models import DeploymentOrder, ENV, STATUS, TYPE


class DeploymentOrderFilter(django_filters.rest_framework.FilterSet):
    '''
    上线单过滤
    '''

    project = django_filters.CharFilter(field_name='project__name', lookup_expr='icontains')
    env = django_filters.ChoiceFilter(choices=ENV)
    status = django_filters.ChoiceFilter(choices=STATUS)
    type = django_filters.ChoiceFilter(choices=TYPE)
    applicant = django_filters.CharFilter(field_name='applicant__name', lookup_expr='icontains')
    reviewer = django_filters.CharFilter(field_name='reviewer__name', lookup_expr='icontains')
    assign_to = django_filters.CharFilter(field_name='assign_to__name', lookup_expr='icontains')

    class Meta:
        model = DeploymentOrder
        fields = ['project', 'env', 'status', 'type', 'applicant', 'reviewer', 'assign_to']