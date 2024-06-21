from django.shortcuts import render

from accounts import models
from fiction import models
from search import models

def home(request):
    context = {}
    return render(request, 'home.html', context)