from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ZimbabweEconomicData, RwandaEconomicData

# Zimbabwe Economic Data CRUD Views
class ZimbabweEconomicDataListView(ListView):
    model = ZimbabweEconomicData
    template_name = 'diplomacy/zimbabwe_economic_list.html'
    context_object_name = 'data'

class ZimbabweEconomicDataCreateView(CreateView):
    model = ZimbabweEconomicData
    template_name = 'diplomacy/zimbabwe_economic_form.html'
    fields = ['date', 'central_bank_rate', 'reserve_money', 'broad_money_m3',
              'usd_yoy_inflation', 'zwg_mom_inflation', 'usd_mom_inflation',
              'official_exchange_rate', 'parallel_exchange_rate', 'monthly_trade_balance']
    success_url = reverse_lazy('zimbabwe-economic-list')

class ZimbabweEconomicDataUpdateView(UpdateView):
    model = ZimbabweEconomicData
    template_name = 'diplomacy/zimbabwe_economic_form.html'
    fields = ['date', 'central_bank_rate', 'reserve_money', 'broad_money_m3',
              'usd_yoy_inflation', 'zwg_mom_inflation', 'usd_mom_inflation',
              'official_exchange_rate', 'parallel_exchange_rate', 'monthly_trade_balance']
    success_url = reverse_lazy('zimbabwe-economic-list')

class ZimbabweEconomicDataDeleteView(DeleteView):
    model = ZimbabweEconomicData
    template_name = 'diplomacy/zimbabwe_economic_confirm_delete.html'
    success_url = reverse_lazy('zimbabwe-economic-list')


# Rwanda Economic Data CRUD Views
class RwandaEconomicDataListView(ListView):
    model = RwandaEconomicData
    template_name = 'diplomacy/rwanda_economic_list.html'
    context_object_name = 'data'

class RwandaEconomicDataCreateView(CreateView):
    model = RwandaEconomicData
    template_name = 'diplomacy/rwanda_economic_form.html'
    fields = ['date', 'rwanda_yoy_inflation', 'official_exchange_rate', 'monthly_trade_balance']
    success_url = reverse_lazy('rwanda-economic-list')

class RwandaEconomicDataUpdateView(UpdateView):
    model = RwandaEconomicData
    template_name = 'diplomacy/rwanda_economic_form.html'
    fields = ['date', 'rwanda_yoy_inflation', 'official_exchange_rate', 'monthly_trade_balance']
    success_url = reverse_lazy('rwanda-economic-list')

class RwandaEconomicDataDeleteView(DeleteView):
    model = RwandaEconomicData
    template_name = 'diplomacy/rwanda_economic_confirm_delete.html'
    success_url = reverse_lazy('rwanda-economic-list')
