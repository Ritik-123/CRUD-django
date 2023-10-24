from django.urls import path
from .views import StudentDetail

urlpatterns = [
    path('student/', StudentDetail.as_view())
]