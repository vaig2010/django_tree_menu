from django.shortcuts import render

def index(request):
    context = {
        "title": "Index page",
    }
    return render(request, "menu_app/index.html", context)


def home(request):
    context = {
        "title": "Home",
    }
    return render(request, "menu_app/home.html", context)


def about(request):
    context = {
        "title": "About page",
    }
    return render(request, "menu_app/about.html", context)


def web_design(request):
    context = {
        "title": "Web design",
    }
    return render(request, "menu_app/web_design.html", context)


def seo(request):
    context = {
        "title": "SEO page",
    }
    return render(request, "menu_app/seo.html", context)


def marketing(request):
    context = {
        "title": "Marketing",
    }
    return render(request, "menu_app/marketing.html", context)


def contact(request):
    context = {
        "title": "Contact",
    }
    return render(request, "menu_app/contact.html", context)


def privacy_policy(request):
    context = {
        "title": "Privacy policy",
    }
    return render(request, "menu_app/privacy_policy.html", context)
