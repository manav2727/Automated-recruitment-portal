from django.urls import path
from .views import list_view, sde_view, finance_view

app_name = 'domain'

urlpatterns = [
    path('', list_view, name='main-domain-view'),
    path('sde/', sde_view, name='sde-domain-view'),
    path('finance/', finance_view, name='finance-domain-view'),
]
