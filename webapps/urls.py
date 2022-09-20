from django.urls import path 
from . import views 

app_name = 'web'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logoutuser/', views.logout_user, name='logoutuser')
]