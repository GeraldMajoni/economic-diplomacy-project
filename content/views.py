from django.shortcuts import render
from .models import AboutApplication, ContactDetails

def about_application(request):
    about = AboutApplication.objects.first()  # Returns None if no instance exists
    return render(request, 'about_application.html', {'about': about})

def contact_us(request):
    # Retrieve the first (or only) ContactDetails instance
    contact = ContactDetails.objects.first()
    return render(request, 'contact_us.html', {'contact': contact})
