# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from hci.helper import Data


@login_required(login_url="/login/")
def index(request):
    get_data = Data()
    Instances = get_data.get_instance_count()
    Jobs = get_data.get_jobs_count()
    Tasks = get_data.get_task_count()
    JobList = get_data.get_jobs()
    InstancesList = get_data.get_instances()

    context = {'segment': 'index',
               'Instances': Instances,
               'Jobs': Jobs,
               'Tasks': Tasks,
               'JobList': JobList,
               'InstancesList': InstancesList}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
