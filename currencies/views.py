from __future__ import unicode_literals
from currencies.models import Currency
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "base.html"
    
    def get_queryset(self):
        return Currency.objects.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the currencies
        context["currencies"] = self.get_queryset()
        return context

class CurrencyDetailView(TemplateView):
    template_name = "detail.html"
    
    def get(self, request, currency_code):
        context = {}
        
        try:
            context["currency"] = Currency.objects.get(Code=currency_code.upper())
        except Currency.DoesNotExist:
            raise Http404("Currency does not exist")
        
        return render(request, self.template_name, context)