from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from src.company.forms import CreateCompanyForm


class RegistrationCompanyView(LoginRequiredMixin, CreateView):
    template_name = 'company/add_company.html'
    form_class = CreateCompanyForm

    def get_success_url(self, tag):
        return reverse('company', args=tag)

    def form_valid(self, form):
        company = form.save(commit=False)
        company.captain = self.request.user
        company.save()
        return redirect(self.get_success_url(tag=form.tag))


class CompanyDetailView(DetailView):
    template_name = 'company/company_detail.html'
