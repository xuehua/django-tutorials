from django.contrib import admin
from .models import (State, City, FirmLocation, Employee, Firm)
# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')

@admin.register(FirmLocation)
class FirmLocationAdmin(admin.ModelAdmin):
    list_display = ('firm', 'city', 'street')

@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    pass
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'firm', 'firm_location')
    search_fields = ('firm', 'firm_location')