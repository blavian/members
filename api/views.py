from rest_framework import generics
from project.models import Members
from .serializers import MembersSerializer

class MemberAPIView(generics.RetrieveAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

class MemberCreateView(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer