from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    '''
    自定义分页
    '''
    page_size = 10
    page_size_query_param = 'size'
    # page_query_param = 'p'
    max_page_size = 99999


class MatchAllPagination(PageNumberPagination):
    '''
    自定义分页, 适用于select下的场景
    '''
    page_size = 1000
    page_size_query_param = 'size'
    # page_query_param = 'p'
    max_page_size = 100000