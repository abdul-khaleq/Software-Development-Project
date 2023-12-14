from django.urls import path
# from views import contact
from . import views

urlpatterns = [
    path("", views.home),
    path("courses/", views.courses),
    path("about/", views.about),
]