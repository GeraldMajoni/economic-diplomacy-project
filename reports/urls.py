from django.urls import path
from .views import download_report

app_name = 'reports'

urlpatterns = [
    path('download/', download_report, name='download_report'),
]
