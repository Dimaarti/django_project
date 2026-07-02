import contextlib

from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination, _positive_int
from rest_framework.response import Response


class UsersListPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'current_page': self.page.number,
            'page_size': self.page_size,
            'pages': self.page.paginator.count // self.page_size + 1,
            'results': data,
        })


class CustomPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50
