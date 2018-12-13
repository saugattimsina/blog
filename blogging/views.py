from django.shortcuts import render
from django.http import HttpResponse
from .models import Author
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    article = Author.objects.all().order_by("date")
    return render(request, "homepage.html", {'article': article})


def detail(request, slug):
    articles = Author.objects.get(slug=slug)
    return render(request,"article_detail.html", {'articles':articles})