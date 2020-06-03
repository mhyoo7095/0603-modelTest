from django.shortcuts import render
from .models import Article


# Create your views here.

def home(requests):
    article = Article.objects
    return render(requests, 'home.html', {'article':article})
