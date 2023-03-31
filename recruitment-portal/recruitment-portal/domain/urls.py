from django.urls import path
from .views import list_view, sde_view, finance_view, electronics_view, machine_view, gamedev_view, datascience_view

app_name = 'domain'

urlpatterns = [
    path('', list_view, name='main-domain-view'),
    path('sde/', sde_view, name='sde-domain-view'),
    path('finance/', finance_view, name='finance-domain-view'),
    path('electronics/', electronics_view, name='electronics-domain-view'),
    path('machine/', machine_view, name='machine-domain-view'),
    path('gamedev/', gamedev_view, name='gamedev-domain-view'),
    path('datascience/', datascience_view, name='datascience-domain-view'),
]
