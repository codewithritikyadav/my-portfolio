
from django.shortcuts import render

def home(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def skills(request):
    return render(request, "main/skills.html")

def experience(request):
    return render(request, "main/experience.html")

def projects(request):
    return render(request, "main/projects.html")

def contact(request):
    return render(request, "main/contact.html")

def certifications(request):
    return render(request, "main/certifications.html")