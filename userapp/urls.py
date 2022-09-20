from django.urls import path 
from . import views 

app_name = 'user'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('diagnosis/', views.diagonzie_symptoms, name='diagnosis'),
    path('diagnosis-details/', views.diagnosis_details, name='diagnosis-details')
]