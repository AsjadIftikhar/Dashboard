import http.client
import json
import requests


class Data:
    base_url = "http://127.0.0.1:8000"

    def get_instance_count(self):
        r = requests.get(self.base_url + '/apiViewSet/Instances/')
        return r.json()['count']

    def get_jobs_count(self):
        r = requests.get(self.base_url + '/apiViewSet/jobs/')
        return r.json()['count']

    def get_task_count(self):
        r = requests.get(self.base_url + '/apiViewSet/tasks/')
        return r.json()['count']

    def get_jobs(self):
        r = requests.get(self.base_url + '/apiViewSet/jobs/')
        return r.json()['results']

    def get_instances(self):
        r = requests.get(self.base_url + '/apiViewSet/Instances/')
        return r.json()['results']

    def get_tasks(self):
        r = requests.get(self.base_url + '/apiViewSet/tasks/')
        return r.json()['results']
