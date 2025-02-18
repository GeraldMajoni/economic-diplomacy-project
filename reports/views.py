from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.db.models import Max
from diplomacy.models import Company, ZimbabweEconomicData, RwandaEconomicData, Imihigo
import requests, base64

def download_report(request):
    selected_country = request.GET.get('country', 'Zimbabwe')
    
    # Get the 5 most recent companies for the selected country
    recent_companies = Company.objects.filter(country=selected_country).order_by('-date_of_engagement')[:5]
    
    # Retrieve economic data for the most recent month and set report_month accordingly
    if selected_country == "Zimbabwe":
        max_date = ZimbabweEconomicData.objects.aggregate(Max('date'))['date__max']
        if max_date:
            economic_data = ZimbabweEconomicData.objects.filter(date__year=max_date.year, date__month=max_date.month)
            report_month = max_date.strftime("%B %Y")
        else:
            economic_data = ZimbabweEconomicData.objects.none()
            report_month = "Unknown"
    elif selected_country == "Rwanda":
        max_date = RwandaEconomicData.objects.aggregate(Max('date'))['date__max']
        if max_date:
            economic_data = RwandaEconomicData.objects.filter(date__year=max_date.year, date__month=max_date.month)
            report_month = max_date.strftime("%B %Y")
        else:
            economic_data = RwandaEconomicData.objects.none()
            report_month = "Unknown"
    else:
        economic_data = []
        report_month = "Unknown"

    # Retrieve Imihigo records for the same year as economic data (assuming Imihigo has a "year" field)
    if max_date:
        imihigos = Imihigo.objects.filter(year=max_date.year).order_by('quarter')
    else:
        imihigos = Imihigo.objects.none()
    
    # Updated Grafana URL with width=1100 and height=1600
    grafana_url = (
        "http://localhost:3000/render/d/eeco7pg4vp79cd/zimbabwe-economic-overview"
        "?orgId=1"
        "&from=2025-01-12T00%3A00%3A00.000Z"
        "&to=2025-02-10T00%3A00%3A00.000Z"
        "&timezone=browser"
        "&width=1100"
        "&height=2000"
    )
    
    try:
        response = requests.get(grafana_url, timeout=10)
        if response.status_code == 200:
            grafana_image_data = "data:image/png;base64," + base64.b64encode(response.content).decode('utf-8')
        else:
            grafana_image_data = ""
    except Exception as e:
        grafana_image_data = ""
    
    context = {
        'selected_country': selected_country,
        'companies': recent_companies,
        'economic_data': economic_data,
        'imihigos': imihigos,
        'report_month': report_month,
        'grafana_image_data': grafana_image_data,
    }
    
    html_string = render_to_string('report_template.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf_file = html.write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="dashboard_report.pdf"'
    return response
