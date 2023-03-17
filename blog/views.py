from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwarge):
    return render(request, 'index.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def blog_view(request, *args, **kwargs):
    return render(request, 'blog.html', {})