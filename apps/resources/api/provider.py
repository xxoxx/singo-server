import logging
from rest_framework import viewsets
from resources.serializers.provider import ProviderSerializer
from ..models.common import Provider
from common.pagination import MatchAllPagination

logger = logging.getLogger('devops')

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    pagination_class = MatchAllPagination
