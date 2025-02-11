from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Company

# List all companies with filtering by country and status via query parameters
class CompanyListView(ListView):
    model = Company
    template_name = 'diplomacy/company_list.html'
    context_object_name = 'companies'

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.GET.get('country')
        status = self.request.GET.get('status')
        if country:
            queryset = queryset.filter(country=country)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

# Create a new company record
class CompanyCreateView(CreateView):
    model = Company
    template_name = 'diplomacy/company_form.html'
    fields = ['company_name', 'country', 'date_of_engagement', 'business_interests',
              'contact_person', 'contact_number', 'status', 'review']
    success_url = reverse_lazy('company-list')

# Update an existing company record
class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'diplomacy/company_form.html'
    fields = ['company_name', 'country', 'date_of_engagement', 'business_interests',
              'contact_person', 'contact_number', 'status', 'review']
    success_url = reverse_lazy('company-list')

# Delete a company record
class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'diplomacy/company_confirm_delete.html'
    success_url = reverse_lazy('company-list')
