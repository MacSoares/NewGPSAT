from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.evaluations_list, name="home"),
]
