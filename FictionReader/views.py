from django.shortcuts import render

from accounts.models import User
from fiction.models import Fiction
from category.models import Category

def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'home.html', context)