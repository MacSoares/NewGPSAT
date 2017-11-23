from django.shortcuts import render
from api.evaluation import EvaluationApi
from .forms import PostForm

def home(request):

    return render(request, 'web/welcome.html', {})

def list(request):
    return render(request, 'web/list.html', {})

def new(request):
    form = PostForm()
    return render(request, 'web/new.html', {'form':form})

def get_patient(request):
    pass