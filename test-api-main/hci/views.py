from django.shortcuts import render
from .serializers import TaskSerializer, JobSerializer, InstanceSerializer
from rest_framework import viewsets
from .models import *
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Tasks.objects.all()
	serializer_class = TaskSerializer
	filter_backends = [SearchFilter]
	search_fields = ['id']

class JobViewSet(viewsets.ModelViewSet):
	queryset = Jobs.objects.all()
	serializer_class = JobSerializer
	filter_backends = [SearchFilter]
	search_fields = ['id']

class InstanceViewSet(viewsets.ModelViewSet):
	queryset = Instances.objects.all()
	serializer_class = InstanceSerializer
	filter_backends = [SearchFilter]
	search_fields = ['id']

class JobStatus(APIView):
	
	def get(self, request, id):
		job = Jobs.objects.get(id=id)
		_job = []
		_job.append({"Status": job.status})
		return Response(_job)

class AllJobStatus(APIView):
	
	def get(self, request):
		jobs = Jobs.objects.all()
		_job = []
		for job in jobs:
			_job.append({"Status": job.status})
		return Response(_job)

class JobTypes(APIView):
	
	def get(self, request):
		jobs = Jobs.objects.all()
		_job = []
		for job in jobs:
			_job.append({"Job Type": job.type})
		return Response(_job)

class SystemTask(APIView):
	
	def get(self, request):
		tasks = Tasks.objects.filter(type="system")
		_tasks = []
		for task in tasks:
			_tasks.append({"id": task.id})
		return Response(_tasks)

class SystemTaskByID(APIView):
	
	def get(self, request,id):
		tasks = Tasks.objects.filter(type="system",id=id)
		_tasks = []
		for task in tasks:
			_tasks.append({"id": task.id, "Name": task.displayName})
		return Response(_tasks)


##########################################################################################################

#!/usr/bin/env python3

# Script that uses HCI Search API.
# Get a json with information from selected index on HCI.


import argparse
import requests
import ast
import json
import os
import sys
from .models import personData

from NGPIris import WD

personDataObj = personData.objects.order_by('id')[0]
# Creates template based on template. 
def create_template(index, query):
    # with open(f"{WD}/hci/template_query.json", "r") as sample:
    sample = personDataObj.template_query
    data = json.load(sample)
    data["indexName"] = index
    data["queryString"] = query

    dumpyboi = personDataObj.dumpyboi
    
    json.dump(data, dumpyboi, indent=4)


def generate_token(password):
    """Generate a security token from a password"""
    with open(password) as pw:
        admin_pass = str(pw.readline()).strip()
        my_key = requests.post("https://10.248.2.93:8888/auth/oauth/", data={"grant_type": personDataObj.password, "username": personDataObj.username, "password": personDataObj.adminPassword, "scope": personDataObj.scope, 
            "client_secret": personDataObj.client_secret, "client_id": personDataObj.client_id, "realm": personDataObj.realm}, verify=False)
        
        return ast.literal_eval(my_key.text)["access_token"].lstrip()

class queryEndPoint(APIView):
	
	def get(self, request,id,token):
		"""Queries the HCI using a token"""
		mqj = personDataObj.written_query
		json_data = json.load(mqj)
		response = requests.post("https://10.248.2.95:8888/api/search/query", headers={"accept": "application/json", "Authorization": f"Bearer {token}"}, 
								json=json_data, verify=False) 
		return Response(response.text)
		
def query(token):
    """Queries the HCI using a token"""
    mqj = personDataObj.written_query
    json_data = json.load(mqj)
    response = requests.post("https://10.248.2.95:8888/api/search/query", headers={"accept": "application/json", "Authorization": f"Bearer {token}"}, 
                             json=json_data, verify=False) 
    return Response(response.text)

def pretty_query(token):
   """Return the result of a query in json loaded format"""
   return json.loads(query(token))["results"]


# If using index, it searches through all indexes if nothing else is specified. 
def index_lister(token, index="all"):
    if index == "all":
        response = requests.get("https://10.248.2.95:8888/api/search/indexes", headers={"accept": "application/json",
                                "Authorization": f"Bearer {token}"}, verify=False)
        response_string = response.text
        fixed_response = ast.literal_eval(response_string.replace("true", "True").replace("false", "False"))
        return fixed_response

    else:
        response = requests.get("https://10.248.2.95:8888/api/search/indexes", headers={"accept": "application/json",
                                "Authorization": f"Bearer {token}"}, verify=False)
        response_string = response.text
        fixed_response = response_string.replace("true", "True").replace("false", "False")

        to_loop = ast.literal_eval(fixed_response)
        for each_dict in to_loop:
            if each_dict["name"] == index:
                return each_dict


def main():
    parser = argparse.ArgumentParser(prog="Fetch information from the HCI")
    
    subparsers = parser.add_subparsers(help="help for subcommand")

    parser_query = subparsers.add_parser("query", help="Query the specified index")
    parser_query.set_defaults(which="query")
    parser_query.add_argument("-q", "--query", nargs="?", action="store", type=str, help="Specify search query, e.g. sample name")
    parser_query.add_argument("-i", "--index", nargs="?", action="store", type=str, help="Specify index from HCI to parse")
    parser_query.add_argument("-o", "--output", nargs="?", action="store", type=str, help="Specify file to store outputs") 
    parser_query.add_argument("-p", "--password", nargs="?", action="store", type=str, help="Specify file to store outputs") 

    parser_index = subparsers.add_parser("index", help="List all queryable indexes and their available fields")
    parser_index.set_defaults(which="index")
    parser_index.add_argument("-i", "--index", nargs="?", action="store", type=str, help="Specify index from HCI to parse, if 'all' list every index and fields")
    parser_index.add_argument("-o", "--output", nargs="?", action="store", type=str, help="Specify file to store outputs") 
    parser_index.add_argument("-p", "--password", nargs="?", action="store", type=str, help="Specify file to store outputs") 

    args = parser.parse_args()
   

    if args.which == "query":        
        create_template(args)
        token = generate_token(args)
        pretty = json.loads(query(token, args.index))
        if args.output:
            with open(args.output, "w+") as result:
                result.write(json.dumps(pretty, indent=4))
        else:
            print(json.dumps(pretty, indent=4))

    elif args.which == "index":
        token = generate_token(args)
        index_list = index_lister(token, index=args.index)
        pretty = json.dumps(index_list)
        if args.output:
            with open(args.output, "w+") as result:
                result.write(json.dumps(pretty, indent=4))
        else:
            print(json.dumps(pretty, indent=4))
        

if __name__ == "__main__":
    main()