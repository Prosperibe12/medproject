from django import forms 
from .models import Patient 

class PatientForm(forms.ModelForm):
    
    first_name = forms.CharField(label=('Firstname'), widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Firstname'}))
    last_name = forms.CharField(label=('Lastame'), widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lastname'}))
    username = forms.CharField(label=('username'), widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email = forms.CharField(label=('Email'), widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    dob = forms.CharField(label=('Date'), widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    phone = forms.CharField(label=('Phone No'), widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}))
    password1 = forms.CharField(label=('Password'), widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(label=('Confirm Password'), widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    
    class Meta:
        model = Patient
        fields = ['first_name','last_name','username','email','gender','dob','phone']
        widgets = {
            'gender': forms.Select(attrs={'class':'form-select'})
        }
        
    # validate form fields
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == "":
            raise forms.ValidationError('This Field Cannot be Empty')
        
        for usernames in Patient.objects.all():
            if usernames.username == username:
                raise forms.ValidationError(f'{username} Already Exist')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == "":
            raise forms.ValidationError("This Field Cannot be Empty")
        
        for emails in Patient.objects.all():
            if emails.email == email:
                raise forms.ValidationError(f'{email} already Exist.')
        return email