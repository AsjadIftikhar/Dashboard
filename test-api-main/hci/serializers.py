from django.db.models import fields
from .models import *
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tasks
		fields = '__all__'
	
class JobSerializer(serializers.ModelSerializer):
	class Meta:
		model = Jobs
		fields = '__all__'

class InstanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Instances
		fields = '__all__'