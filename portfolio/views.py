from django.shortcuts import render
import portfolio.views
from .models import Portfolio

def portfolio(request):
    portfolio = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolio}) 