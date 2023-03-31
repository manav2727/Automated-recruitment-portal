from django.contrib import admin
from .models import Domains, Sde, Finance, Electronics, Machine, Gamedev, Datascience

# Register your models here.
admin.site.register(Domains)
admin.site.register(Sde)
admin.site.register(Finance)
admin.site.register(Electronics)
admin.site.register(Machine)
admin.site.register(Gamedev)
admin.site.register(Datascience)
