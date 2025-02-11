# diplomacy/views_imihigo.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Imihigo

class ImihigoListView(ListView):
    model = Imihigo
    template_name = 'diplomacy/imihigo_list.html'
    context_object_name = 'imihigos'

    def get_queryset(self):
        # Return only the top 4 records sorted by quarter (or another appropriate criterion)
        return Imihigo.objects.all().order_by('quarter')[:4]

class ImihigoCreateView(CreateView):
    model = Imihigo
    template_name = 'diplomacy/imihigo_form.html'
    fields = ['quarter', 'baseline_target', 'actual_result', 'comments']
    success_url = reverse_lazy('imihigo-list')

class ImihigoUpdateView(UpdateView):
    model = Imihigo
    template_name = 'diplomacy/imihigo_form.html'
    fields = ['quarter', 'baseline_target', 'actual_result', 'comments']
    success_url = reverse_lazy('imihigo-list')

class ImihigoDeleteView(DeleteView):
    model = Imihigo
    template_name = 'diplomacy/imihigo_confirm_delete.html'
    success_url = reverse_lazy('imihigo-list')
