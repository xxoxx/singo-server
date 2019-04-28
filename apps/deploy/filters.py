__author__ = 'singo'
__datetime__ = '2019/4/28 11:11 AM '


import django_filters
from .models import DeploymentOrder


class DeploymentOrderFilter(django_filters.rest_framework.FilterSet):
    '''
    上线单过滤git
    '''
    ENV = (
        (0, '生产'),
        (1, '预发布'),
        (2, '测试')
    )
    project = django_filters.CharFilter(field_name='project__name', lookup_expr='icontains')
    env = django_filters.ChoiceFilter(choices=ENV)
    applicant = django_filters.CharFilter(field_name='applicant__name', lookup_expr='icontains')
    reviewer = django_filters.CharFilter(field_name='reviewer__name', lookup_expr='icontains')
    assign_to = django_filters.CharFilter(field_name='assign_to__name', lookup_expr='icontains')

    class Meta:
        model = DeploymentOrder
        fields = ['project', 'env', 'applicant', 'reviewer', 'assign_to']