
from django.http import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


AREA_CODE = 2  # 0 space , 1 namespace , 2 tenant


@login_required(login_url='/login/')
def main(request, pk):
    area_code = AREA_CODE
    return render('tenant.html', locals())


@api_view(['GET'])
def get_tenants(request):
    context = {}
    return render(request, 'templates/themes/index.html', context)


def login(request):
    context = {}
    return render(request, 'templates/themes/login.html', context)


def home(request):
    context = {}
    return render(request, 'templates/themes/index.html', context)
