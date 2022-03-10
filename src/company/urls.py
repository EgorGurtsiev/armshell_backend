from django.urls import path
from .views import RegistrationCompanyView


urlpatterns = [
    path('registration/', RegistrationCompanyView.as_view(), name='add_company'),
]