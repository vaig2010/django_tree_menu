# app/views.py
from django.shortcuts import render
from .models import Menu

def index(request):
    return render(request, 'menu_app/index.html', {'menus': Menu.objects.all()})

def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'menu_app/home.html', context)

def about(request):
    return render(request, 'menu_app/about.html')

def web_design(request):
    return render(request, 'menu_app/web_design.html')

def seo(request):
    return render(request, 'menu_app/seo.html')

def marketing(request):
    return render(request, 'menu_app/marketing.html')

def contact(request):
    return render(request, 'menu_app/contact.html')

def privacy_policy(request):
    return render(request, 'menu_app/privacy_policy.html')