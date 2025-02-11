# analytics/urls.py
app_name = 'analytics'

from django.urls import path
from .views import PredictiveAnalyticsView, chatbot_view, TrainModelView
from .views import grafana_dashboard
from .views import grafana_link

urlpatterns = [
    path('train/', TrainModelView.as_view(), name='train-model'),
    path('predict/', PredictiveAnalyticsView.as_view(), name='predictive'),
    path('chat/', chatbot_view, name='chatbot'),
    path('grafana/', grafana_dashboard, name='grafana-dashboard'),
    path('grafana-link/', grafana_link, name='grafana-link'),
]
