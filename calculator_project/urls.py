from django.urls import path
from calculator_app.views import CalculatorView

urlpatterns = [
    path('add/', CalculatorView.as_view(), {'operation': 'add'}),
    path('sub/', CalculatorView.as_view(), {'operation': 'sub'}),
    path('mul/', CalculatorView.as_view(), {'operation': 'mul'}),
    path('div/', CalculatorView.as_view(), {'operation': 'div'}),
]
