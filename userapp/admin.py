from django.contrib import admin
from .models import PatientWaitList, Doctors, Symptoms
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import path
from django.shortcuts import render
from django.urls import reverse
from django import forms

# Register your models here.

class PatientForm(forms.Form):
    csv_upload = forms.FileField()
    
class DoctorForm(forms.Form):
    csv_upload = forms.FileField()
    
class SymtomsForm(forms.Form):
    csv_upload = forms.FileField()
    
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'specialty',
        'phone',
        'medical_code',
        'years_of_experience'
    )
    
    # get all urls under this model and add custom urls
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    
    def upload_csv(self, request):

        form = DoctorForm()
        # process form
        if request.method == 'POST':
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            for x in csv_data:
                fields = x.split(",")
                created = Doctors.objects.update_or_create(
                    first_name = fields[0],
                    last_name = fields[1],
                    email = fields[2],
                    specialty = fields[3],
                    phone = fields[4],
                    medical_code = fields[5],
                    years_of_experience = fields[6]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)                
        
        data = {
            'form':form
        }
        return render(request, 'admin/csv_upload.html', data)
    
class PatientWaitListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'gender',
        'dob',
        'phone'
    )

    # get all urls under this model and add custom urls
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-file/', self.upload_file),]
        return new_urls + urls
    
    def upload_file(self, request):

        form = PatientForm()
        # process form
        if request.method == 'POST':
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            for x in csv_data:
                fields = x.split(",")
                created = PatientWaitList.objects.update_or_create(
                    first_name = fields[0],
                    last_name = fields[1],
                    email = fields[2],
                    gender = fields[3],
                    dob = fields[4],
                    phone = fields[5]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)
        
        data = {
            'form':form
        }
        return render(request, 'admin/file_upload.html', data)
    
class SymptomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'illness',
        'manifest1',
        'manifest2',
        'manifest3',
        'manifest4',
        'manifest5',
        'manifest6',
        'manifest7',
        'manifest8',
        'manifest9',
        'manifest10',
        'manifest11',
        'manifest12'
    )
    
     # get all urls under this model and add custom urls
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-symptoms/', self.upload_symptom),]
        return new_urls + urls
    
    def upload_symptom(self, request):
        
        form = SymtomsForm()
        # process form
        if request.method == 'POST':
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            for x in csv_data:
                fields = x.split(",")
                created = Symptoms.objects.update_or_create(
                    illness = fields[0],
                    manifest1 = fields[1],
                    manifest2 = fields[2],
                    manifest3 = fields[3],
                    manifest4 = fields[4],
                    manifest5 = fields[5],
                    manifest6 = fields[6],
                    manifest7 = fields[7],
                    manifest8 = fields[8],
                    manifest9 = fields[9],
                    manifest10 = fields[10],
                    manifest11 = fields[11],
                    manifest12 = fields[12]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)                
        
        data = {
            'form':form
        }
        return render(request, 'admin/symptoms_upload.html', data)
    
admin.site.register(Symptoms, SymptomAdmin)
admin.site.register(PatientWaitList, PatientWaitListAdmin)
admin.site.register(Doctors, DoctorAdmin)
