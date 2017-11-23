from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('list', views.list, name="list"),
    path('new', views.new, name="new"),
    path('patient/<int:id>', views.get_patient, name="patient"),
]
