from django.urls import path
from . import views


urlpatterns = [
    path('api/evaluations/', views.Evaluations.as_view(), name="home"),
    path('api/evaluations/<pk>/', views.EvaluationDetail.as_view(), name="home"),
]
