from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

def support(request):
    return HttpResponse("support")

def docs(request):
    return HttpResponse("docs")