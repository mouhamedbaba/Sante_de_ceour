from django.shortcuts import render
from administration.models import Collect
# Create your views here.

def home(request):
    collects = Collect.objects.filter(confirmer = 1, posted = 1, is_amount_reached = 0).order_by('-created_at')[:3]
    context = {
        'collects' : collects
    }
    return render(request, 'landing/pages/index.html', context)

def blog(request):
    return render(request, 'landing/pages/blog.html')