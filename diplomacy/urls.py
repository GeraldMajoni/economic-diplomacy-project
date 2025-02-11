# diplomacy/urls.py
from django.urls import path
from .views_company import (
    CompanyListView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView,
)
from .views_imihigo import (
    ImihigoListView, ImihigoCreateView, ImihigoUpdateView, ImihigoDeleteView,
)
from .views_economic import (
    ZimbabweEconomicDataListView, ZimbabweEconomicDataCreateView,
    ZimbabweEconomicDataUpdateView, ZimbabweEconomicDataDeleteView,
    RwandaEconomicDataListView, RwandaEconomicDataCreateView,
    RwandaEconomicDataUpdateView, RwandaEconomicDataDeleteView,
)

urlpatterns = [
    # Company CRUD URLs
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/create/', CompanyCreateView.as_view(), name='company-create'),
    path('companies/update/<int:pk>/', CompanyUpdateView.as_view(), name='company-update'),
    path('companies/delete/<int:pk>/', CompanyDeleteView.as_view(), name='company-delete'),

    # Imihigo CRUD URLs
    path('imihigo/', ImihigoListView.as_view(), name='imihigo-list'),
    path('imihigo/create/', ImihigoCreateView.as_view(), name='imihigo-create'),
    path('imihigo/update/<int:pk>/', ImihigoUpdateView.as_view(), name='imihigo-update'),
    path('imihigo/delete/<int:pk>/', ImihigoDeleteView.as_view(), name='imihigo-delete'),

    # Zimbabwe Economic Data CRUD URLs
    path('zimbabwe-economic/', ZimbabweEconomicDataListView.as_view(), name='zimbabwe-economic-list'),
    path('zimbabwe-economic/create/', ZimbabweEconomicDataCreateView.as_view(), name='zimbabwe-economic-create'),
    path('zimbabwe-economic/update/<int:pk>/', ZimbabweEconomicDataUpdateView.as_view(), name='zimbabwe-economic-update'),
    path('zimbabwe-economic/delete/<int:pk>/', ZimbabweEconomicDataDeleteView.as_view(), name='zimbabwe-economic-delete'),

    # Rwanda Economic Data CRUD URLs
    path('rwanda-economic/', RwandaEconomicDataListView.as_view(), name='rwanda-economic-list'),
    path('rwanda-economic/create/', RwandaEconomicDataCreateView.as_view(), name='rwanda-economic-create'),
    path('rwanda-economic/update/<int:pk>/', RwandaEconomicDataUpdateView.as_view(), name='rwanda-economic-update'),
    path('rwanda-economic/delete/<int:pk>/', RwandaEconomicDataDeleteView.as_view(), name='rwanda-economic-delete'),
]
