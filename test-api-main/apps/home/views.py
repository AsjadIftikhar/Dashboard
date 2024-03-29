# -*- encoding: utf-8 -*-
from dateutil .relativedelta import relativedelta
"""
Copyright (c) 2019 - present AppSeed.us
"""
import datetime

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
    TaskList = get_data.get_tasks()
    JobListToday = []
    JobListThisWeek = []
    TaskListToday = []
    TaskListThisWeek = []

    for Job in JobList:
        if Job["dueDate"] == str(datetime.date.today()):
            JobListToday.append(Job)

    for Job in JobList:
        if Job["dueDate"] <= str(datetime.date.today() + datetime.timedelta(days=7)):
            JobListThisWeek.append(Job)

    for Task in TaskList:
        if Task["dueDate"] == str(datetime.date.today()):
            TaskListToday.append(Task)

    for Task in TaskList:
        if Task["dueDate"] <= str(datetime.date.today() + datetime.timedelta(days=7)):
            TaskListThisWeek.append(Task)


    context = {'segment': 'index',
               'Instances': Instances,
               'Jobs': Jobs,
               'Tasks': Tasks,
               'JobList': JobList,
               'JobListToday': JobListToday,
               'JobListThisWeek': JobListThisWeek,
               'InstancesList': InstancesList,
               'TaskList': TaskList,
               'TaskListToday': TaskListToday,
               'TaskListThisWeek': TaskListThisWeek}

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
