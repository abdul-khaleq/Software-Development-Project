from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    # path('django_form/', views.djangoForm, name='django_form'),
    # path('django_form/', views.studentForm, name='django_form'),
    path('django_form/', views.passwordValidation, name='django_form'),
]