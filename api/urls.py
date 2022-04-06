from django.urls import path

from .views import MemberAPIView,MemberCreateView

urlpatterns = [
    path('members/<int:pk>', MemberAPIView.as_view()),
    path('members/', MemberCreateView.as_view()),
]