from django.urls import path
from . import views

urlpatterns = [
    path('graph/', views.ChartData.as_view(), name='chart data')
]