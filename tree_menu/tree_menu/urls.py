"""
URL configuration for tree_menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menu_app import views
from debug_toolbar.toolbar import debug_toolbar_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main_menu'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('services/web-development/web-design/', views.web_design, name='web_design'),
    path('services/seo/', views.seo, name='seo'),
    path('services/marketing/', views.marketing, name='marketing'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('<path:path>/', views.draw_menu, name='draw_menu'),
] + debug_toolbar_urls()
