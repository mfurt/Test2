from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Auto


class Index(ListView):
    model = Auto
    queryset = Auto.objects.all()
    template_name = 'index.html'


class SearchResultsView(ListView):
    model = Auto
    template_name = 'search_results.html'

    def get_queryset(self):
        return Auto.objects.filter(
            Q(name__icontains=self.request.GET.get('q')))
