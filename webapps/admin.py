from django.contrib import admin
from .models import *

# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'created_at'
    )
    
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'first_name',
        'last_name',
        'email',
        'gender',
        'dob',
        'phone',
        'date_created'
    )
    
admin.site.register(Banner, BannerAdmin)
admin.site.register(Patient, PatientAdmin)
