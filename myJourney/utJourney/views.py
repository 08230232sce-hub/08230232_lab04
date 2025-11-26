from django.shortcuts import render
from .models import LearningJourney

def home(request):
    journey = LearningJourney.objects.all().order_by('-date')
    return render(request, 'utJourney/index.html', {'journey': journey})

def about(request):
    return render(request, 'utJourney/aboutMe.html')
