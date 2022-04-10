from django.urls import re_path

from .views import MemberAPIView,MemberCreateView

urlpatterns = [
    re_path('members/(?P<pk>\d+)', MemberAPIView.as_view()),
    re_path('members/', MemberCreateView.as_view()),
]