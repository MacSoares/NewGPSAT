from django.urls import path
from . import views


urlpatterns = [
    path('', views.evaluation_list, name="evaluations"),
]
