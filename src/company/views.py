from django.shortcuts import render
from django.views.generic import FormView, CreateView
from .forms import CreateCompanyForm
from .models import Company


class RegdCompany(CreateView):
    model = Company
    template_name = "company/new_company.html"
    form_class = CreateCompanyForm

    def form_valid(self):
        pass

