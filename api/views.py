from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from project.models import Account, Members
from .serializers import MembersSerializer

class MemberAPIView(generics.RetrieveAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

class MemberCreateView(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id','phone_number', 'client_member_id', 'account_id')



