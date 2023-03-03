from django.contrib import admin
from . models import MockIt, Mock

# Register your models here.
admin.site.register(Mock)
admin.site.register(MockIt)