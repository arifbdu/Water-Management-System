# pond_app/admin.py
from django.contrib import admin
from .models import CustomUser, PondData

admin.site.register(CustomUser)
admin.site.register(PondData)
