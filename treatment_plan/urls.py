from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="treatment_plan-home")
]