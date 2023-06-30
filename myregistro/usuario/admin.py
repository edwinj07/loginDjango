from django.contrib import admin
from .models import Persona

# Register your models here.
# class PersonAdmin(admin.ModelAdmin):
#     readonly_fields=("cc",)

admin.site.register(Persona)