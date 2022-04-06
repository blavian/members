from django.urls import path

from .views import MemberAPIView

urlpatterns = [
    path('<int:pk>', MemberAPIView.as_view()),
]