from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import list_view, dbms_view

app_name = "mock"

urlpatterns = [
    path("", list_view, name="main-mock-view"),
    path('dbms/', dbms_view, name='dbms-mock-view'),
]