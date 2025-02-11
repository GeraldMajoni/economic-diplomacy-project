from django.urls import path
from .views import about_application, contact_us

app_name = 'content'

urlpatterns = [
    path('about/', about_application, name='about-application'),
    path('contact/', contact_us, name='contact-us'),
]
