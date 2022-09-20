from sqlite3 import IntegrityError
from django.shortcuts import render,  redirect
from django.contrib.auth.decorators import login_required 
from .models import * 
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q 
import infermedica_api 
from django.conf import settings
import wikipedia 


# Create your views here.
@login_required(login_url='web:login')
def dashboard_view(request):     
    
    if request.method == 'POST':
        # get parameters from request body
        api = infermedica_api.APIv3Connector(app_id=settings.APPLICATION_ID, app_key=settings.APPLICATION_KEY)
        # r = api.get_diagnostic_data_dict()
        age = int(request.POST.get('age'))
        sex = request.POST.get('sex')
        response = api.parse(f'{request.POST.get("symptoms")}', age=age)
        response = api.parse(
            f'{request.POST.get("symptoms")}', age=age, include_tokens=True
        )
        # print(response, end="\n\n")
        if response:
            request.session['age'] = age 
            request.session['sex'] = sex 
            request.session['result_diagonize'] = response
            return redirect('user:diagnosis')
        
    context = {
        'Title':'Dasboard'
    }
    return render(request, 'userapp/dashboard.html', context)

# diagonize symptoms
@login_required(login_url='web:login')
def diagonzie_symptoms(request):
    
    # get session response
    age = request.session.get('age', None)
    sex = "female"
    
    # process response to symptoms 
    if request.method == 'GET':
        symptom1 = request.GET.get('symptoms')
        symptom2 = request.GET.get('symptom1')
        print("symptom 1", symptom1)
        print("symptom 2", symptom2)
        
        results = Symptoms.objects.filter(Q(manifest1__iexact=symptom1) | Q(manifest2__iexact=symptom1) | Q(manifest3__iexact=symptom2) | Q(manifest4__iexact=symptom2) | Q(manifest5__iexact=symptom1) | Q(manifest6__iexact=symptom1) | Q(manifest7__iexact=symptom1) | Q(manifest8__iexact=symptom2) | Q(manifest9__iexact=symptom2) | Q(manifest10__iexact=symptom1) | Q(manifest11__iexact=symptom1) | Q(manifest12__iexact=symptom1))
                    
    context = {
        'Title': 'Diagnosis',
        'result_diagonize':results
    }
    return render(request, 'userapp/diagnosis.html', context)

# read details of illness
@login_required(login_url='web:login')
def diagnosis_details(request):
    
    # get disease via url
    data = request.GET.get('read')
    try:
        data = wikipedia.summary(f'{data}', sentences = 7)
    except IntegrityError:
        # not sure of this: change later
        return redirect('user:dashboard')
    if data:
        result = data 
    # query for doctor
    doctor = Doctors.objects.order_by('?')[0]
    # prepare mail : this would have been done using a message broker and celery but i'm utilizing a free service
    html_content = render_to_string('userapp/email.html', {
        'name': request.user.patient.first_name,
        'first_name':doctor.first_name,
        'last_name':doctor.last_name,
        'email':doctor.email,
        'specialty':doctor.specialty,
        'phone':doctor.phone,
        'medical_code':doctor.medical_code,
        'years_of_experience':doctor.years_of_experience
    })
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives("RECOVERY PLAN", text_content, settings.EMAIL_HOST_USER, [request.user.patient.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    context = {
        'result':result
    }
    return render(request, 'userapp/diagnosis-details.html', context)

# function for profile page
@login_required(login_url='web:login')
def profile_view(request):
    
    profile = request.user.patient
    data = {
        'Title': 'Profile Page',
        'profile': profile
    }
    return render(request, 'userapp/profile.html', data)


