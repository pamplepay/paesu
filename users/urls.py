from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('changeInfo/', views.ChageInfo, name='changeinfo'),

    path('api/v1/id-validation', views.IdValidation.as_view(), name='id_validation'), 
    # path('api/v1/hp-validation', views.HPValidation.as_view(), name='hp_validation'), 
    path('api/v1/email-validation', views.EmailValidation.as_view(), name='email_validation'), 
]