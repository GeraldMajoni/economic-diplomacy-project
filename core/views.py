from django.shortcuts import render
from datetime import date
from diplomacy.models import Company, ZimbabweEconomicData, RwandaEconomicData, Imihigo

def about_application(request):
    return render(request, 'about_application.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def dashboard_view(request):
    if request.user.is_superuser:
        return render(request, 'dashboard_superuser.html')
    
    country = request.GET.get('country', 'Zimbabwe')
    year_filter = request.GET.get('year')
    if not year_filter or year_filter == "":
        year_filter = date.today().year
    else:
        year_filter = int(year_filter)
    
    recent_companies = Company.objects.filter(country=country).order_by('-date_of_engagement')[:5]
    if country == 'Zimbabwe':
        recent_economic = ZimbabweEconomicData.objects.order_by('-date')[:5]
    elif country == 'Rwanda':
        recent_economic = RwandaEconomicData.objects.order_by('-date')[:5]
    else:
        recent_economic = None

    imihigos = Imihigo.objects.filter(year=year_filter).order_by('quarter')

    context = {
        'recent_companies': recent_companies,
        'recent_economic': recent_economic,
        'imihigos': imihigos,
        'selected_country': country,
        'selected_year': year_filter,
    }
    return render(request, 'dashboard_normal_user.html', context)
