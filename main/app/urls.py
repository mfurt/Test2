from django.urls import path
from .views import Index,SearchResultsView

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='result')
]