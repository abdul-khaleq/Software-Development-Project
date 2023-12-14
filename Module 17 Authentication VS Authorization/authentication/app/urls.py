from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.userLogOut, name='logout'),
    path('pass_change/', views.pass_change, name='passchange'),
    path('pass_change2/', views.pass_change2, name='passchange2'),
]
