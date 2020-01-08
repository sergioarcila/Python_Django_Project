from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login
import uuid

User = get_user_model()


# Create your views here.
def home(request):
    return render(request, 'gen/home.html')


def view_profile(request, uuid):
    context = {
        'profile': PlayerProfile.objects.get(id=uuid)
    }
    return render(request, 'profiles/view_profile.html', context)
