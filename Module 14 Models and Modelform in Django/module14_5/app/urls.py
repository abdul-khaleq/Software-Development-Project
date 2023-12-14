from django.urls import path
# from . import views
from app.views import home

urlpatterns = [
    #  path('', views.home, name='homepage'),
     path('', home, name='homepage'),
]
