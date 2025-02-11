from django.contrib import admin
from django.urls import path, include
from core.views import dashboard_view
from core.views import about_application
from core.views import contact_us

urlpatterns = [
    path('about/', about_application, name='about-application'),
    path('contact/', contact_us, name='contact-us'),
    path('admin/', admin.site.urls),
    path('userauth/', include('userauth.urls')),
    path('diplomacy/', include('diplomacy.urls')),
    path('analytics/', include('analytics.urls')),  # This should pick up the app_name automatically
    path('', dashboard_view, name='dashboard'),
    path('content/', include('content.urls')),  # Include content app URLs
]
