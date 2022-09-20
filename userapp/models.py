from django.db import models

# Create your models here.
# patients waitlist model
class PatientWaitList(models.Model):
    
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    dob = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.first_name

# Doctors model
class Doctors(models.Model):
    
    first_name  = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    specialty = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=150, blank=True, null=True)
    medical_code = models.CharField(max_length=150, blank=True, null=True)
    years_of_experience = models.CharField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return self.first_name
    
# Illness and symtopms model
class Symptoms(models.Model):
    
    illness = models.CharField(max_length=200, blank=True, null=True)
    manifest1 = models.CharField(max_length=200, blank=True, null=True)
    manifest2 = models.CharField(max_length=200, blank=True, null=True)
    manifest3 = models.CharField(max_length=200, blank=True, null=True)
    manifest4 = models.CharField(max_length=200, blank=True, null=True)
    manifest5 = models.CharField(max_length=200, blank=True, null=True)
    manifest6 = models.CharField(max_length=200, blank=True, null=True)
    manifest7 = models.CharField(max_length=200, blank=True, null=True)
    manifest8 = models.CharField(max_length=200, blank=True, null=True)
    manifest9 = models.CharField(max_length=200, blank=True, null=True)
    manifest10 = models.CharField(max_length=200, blank=True, null=True)
    manifest11 = models.CharField(max_length=200, blank=True, null=True)
    manifest12 = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.illness
