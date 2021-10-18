from django.contrib import admin

from .models import Customer, FitnessPlan

admin.site.register(FitnessPlan)
admin.site.register(Customer)
