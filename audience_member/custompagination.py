from rest_framework.pagination import LimitOffsetPagination

class UpperBoundPagination(LimitOffsetPagination):
    max_limit = 100
