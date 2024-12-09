from django.contrib import admin

from .models import Pet, Appointment

# Register your models here.
admin.site.register(Pet)
admin.site.register(Appointment)
