from django.contrib.auth import models
from rest_framework import serializers
from django.contrib.auth.models import User
from management.models import *
from .models import *
class TenantCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    systemVisibleDescription = serializers.CharField(max_length=255)
    hardQuota = serializers.CharField(max_length=255)
    softQuota = serializers.CharField(max_length=255)
    namespaceQuota = serializers.CharField(max_length=255)
    complianceConfigurationEnabled = serializers.BooleanField(default=False)
    versioningConfigurationEnabled = serializers.BooleanField(default=False)
    searchConfigurationEnabled = serializers.BooleanField(default=False)
    replicationConfigurationEnabled = serializers.BooleanField(default=False)
    servicePlanSelectionEnabled = serializers.BooleanField(default=False)
    servicePlan = serializers.CharField(max_length=255,required=False)

class NamespaceCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    hashScheme = serializers.CharField(max_length=255)
    enterpriseMode = serializers.BooleanField(default=False)
    hardQuota = serializers.CharField(max_length=255)
    softQuota = serializers.CharField(max_length=255)
    aclsUsage = serializers.CharField(max_length=255)
    searchEnabled = serializers.BooleanField(default=False)
    indexingEnabled = serializers.BooleanField(default=False)
    customMetadataIndexingEnabled = serializers.BooleanField(default=False)
    replicationEnabled = serializers.BooleanField(default=False)
    readFromReplica = serializers.BooleanField(default=False)
    serviceRemoteSystemRequests = serializers.BooleanField(default=False)


class NameSpacesSerializer(serializers.ModelSerializer):
    fileurl= serializers.ReadOnlyField(source='NameSpaces.fileurl')
    # id= serializers.ReadOnlyField(source='NameSpaces.uuid')
    class Meta:
        model = NameSpaces
        fields = ['namespaces_name', 'namespaces_ref','tenantz','files','fileurl','uuid']

class NameSpacesSerializer2(serializers.ModelSerializer):
    # fileurl= serializers.ReadOnlyField(source='NameSpaces.fileurl')
    # id= serializers.ReadOnlyField(source='NameSpaces.uuid')
    class Meta:
        model = NameSpaces
        fields = ['namespaces_name', 'namespaces_ref','tenantz']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = ['regions_name', 'regions_ref']
    
class TenantsSerializer(serializers.ModelSerializer):
    # regionz= serializers.ReadOnlyField(source='regionz.regions_name')
    class Meta:
        model = Tenants
        fields = ['tenants_name', 'tenants_ref', 'regionz']


class integerSerializer(serializers.ModelSerializer):
    class Meta:
        model = integerTable
        fields = ['id', 'address', 'username', 'password', 'regions']

class NamespaceSerialize(serializers.Serializer):
    namespaces_name = serializers.CharField(max_length=100)
    namespaces_ref = serializers.CharField(max_length=100)

class GetTenantsSerialize(serializers.Serializer):
    tenants_name = serializers.CharField(max_length=100)
    tenants_ref = serializers.CharField(max_length=100)
    

class RegionsSerialize(serializers.Serializer):
    regions_name = serializers.CharField(max_length=100)
    regions_ref = serializers.CharField(max_length=100)

