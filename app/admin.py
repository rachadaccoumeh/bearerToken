from django.contrib import admin
from .models import *


# Register your models here.


class MedicalTestAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'hospital', 'description', 'doctor', 'patient', 'private', 'completed']


class HospitalAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_editable = ['phone']
    list_display = ['name', 'phone', 'location']


admin.site.register(MedicalTest, MedicalTestAdmin)
admin.site.register(Hospital, HospitalAdmin)


class LocationAdmin:
    list_display = ['zip', 'state', 'abr_location', 'address']


admin.site.register(Location)
admin.site.register(EmailVerification)
admin.site.register(PhoneVerification)
