from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from uygulama import models


def index(request):
    return HttpResponse("BLOG")