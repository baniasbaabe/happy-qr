from django.urls import path, include

from crm import views

urlpatterns = [
    path('', views.dashboard, name='crm_dashboard'),
    path('kundenliste', views.kundenliste, name='kundenliste'),
]
