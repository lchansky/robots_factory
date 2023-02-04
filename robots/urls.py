from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/create', API.as_view()),
    path('weekly_report', download_last_week_report),
]
