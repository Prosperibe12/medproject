from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Banner(models.Model):
    
    image = models.ImageField(upload_to='banners')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.image}'

class Patient(models.Model):
    
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=50, choices=GENDER)
    dob = models.DateField()
    phone = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name