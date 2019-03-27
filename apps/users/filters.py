from rest_framework import generics
import django_filters
from .models import User, UserGroup


# class UserProfileFilter(django_filters.FilterSet):
class UserProfileFilter(django_filters.rest_framework.FilterSet):
    '''
    用户过滤
    '''
    username = django_filters.CharFilter(lookup_expr='icontains')
    role = django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()
    is_staff = django_filters.BooleanFilter()
    # max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = User
        fields = ['username', 'role', 'is_active', 'is_staff']