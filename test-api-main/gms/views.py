from django.shortcuts import render
from .serializers import NameSpacesSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import NameSpaces

from rest_framework import status, views
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.http import *
import requests
from .serializers import *
from .models import *
import coreapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
# from .serializer import MyModelSerializer
from NGPIris import WD
from .hcp import HCPManager
import os
import uuid
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


def main(request):
    return HttpResponseRedirect('docs/')


@api_view(['GET'])
def get_spaces(request):
    return HttpResponseRedirect('docs/')


# #TODO: Login crediantals must be ok
# @api_view(['GET'])
# def get_tenants(request):

# 	if request.method == 'GET':
# 		#TODO: Tenant user matching
# 		#TODO: Response type not be xml
# 		headers = {'content-type': 'application/json','Authorization': 'HCP bXNheWdp:65f612d5e6bfba42b9961bf2767e7b5d'}
# 		integerObject = integerTable.objects.get(id = 1)
# 		getURL = integerObject.address+"/mapi/tenants?username="+integerObject.username+"&password="+integerObject.password+"&forcePasswordChange=false"
# 		response = requests.get(
# 			getURL,
# 			headers=headers,
# 			verify=False)
# 		if response.status_code != 200:
# 			return Response(response.headers, status=response.status_code)
# 		else:
# 			return Response(response, status=status.HTTP_200_OK)
# 	else:
# 		return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# @api_view(['POST']) def create_tenants(request): if request.method == 'POST': serializer = TenantCreateSerializer(
# data=request.data) if serializer.is_valid(): #TODO: Tenant user matching headers = {'content-type':
#  'application/json','Authorization': 'HCP bXNheWdp:65f612d5e6bfba42b9961bf2767e7b5d'} integerObject =
#  integerTable.objects.get(id = 1) getURL = integerObject.address+"/mapi/tenants?username="+integerObject.username
#  +"&password="+integerObject.password+"&forcePasswordChange=false" response = requests.put( getURL,
#  json= serializer.data, headers=headers, verify=False) if response.status_code != 200: return Response(
#  response.headers, status=response.status_code) else: return Response(response.headers, status=status.HTTP_200_OK)
#  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) else: return Response(
#  status=status.HTTP_405_METHOD_NOT_ALLOWED)

class GetRegions(viewsets.ModelViewSet):
    queryset = Regions.objects.all()
    serializer_class = RegionSerializer


# class GetTenants(views.APIView):
# 	def get(self,request):
# 		data=Tenants.objects.all()
# 		serializer = TenantsSerializer(data, many=True)
# 		if request.method == 'GET':
# 			print('*'*10,serializer.data)
# 			jsondata = JSONRenderer().render(serializer.data)
# 			return HttpResponse(jsondata, content_type = 'application/json' )
# 		return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GetTenants(viewsets.ModelViewSet):
    queryset = Tenants.objects.all()
    serializer_class = TenantsSerializer


# @api_view(['GET'])
class GetNamespaces(viewsets.ModelViewSet):
    queryset = NameSpaces.objects.all()
    serializer_class = NameSpacesSerializer


class CreateNamespace(generics.CreateAPIView):
    # namespaces = openapi.Parameter('namespaces_name', in_= openapi.IN_QUERY, type= openapi.TYPE_STRING)
    # namespaces_ref = openapi.Parameter('namespaces_ref', in_= openapi.IN_QUERY, type= openapi.TYPE_STRING)
    # tenantz = openapi.Parameter('tenantz', in_= openapi.IN_QUERY, type= openapi.TYPE_STRING)
    # files = openapi.Parameter('files', in_= openapi.IN_QUERY, type= openapi.TYPE_FILE)
    # @swagger_auto_schema(manual_parameters = [namespaces,namespaces_ref,tenantz,files])
    serializer_class = NameSpacesSerializer
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description='Upload file...', )
    @action(detail=False, methods=['post'])
    def post(self, request):
        print('got 0', request)
        print('REQ0', request.data)
        print('req files', request.FILES.get('files'))
        if request.method == 'POST':
            print('got post', request.POST)
            print('got 1', request.GET)
            print('got 2', request.GET.get('files'))
            serializer = NameSpacesSerializer(data=request.data)
            print('searlizer', serializer)
            if serializer.is_valid():
                print('ckecking active', )
                userProfile = Profile.objects.get(user=request.user)
                userPermission = userProfile.permission
                print('userPermission', userPermission)

                instance = serializer.save()
                # instance.files.delete(save= True)
                if userPermission:
                    localfile = str(instance.files)
                    print('scfsd', type(localfile), localfile, os.getcwd())

                    from gms.models import integerTable
                    integer_table = integerTable.objects.get(username=request.user)
                    hcpm = HCPManager(credentials_path=[
                        integer_table.EP, integer_table.AK, integer_table.ASK
                    ], autotest=False)

                    ls = hcpm.list_buckets()
                    print(f"\n\nBuckets: {ls}")
                    hcpm.attach_bucket('elasticbeanstalk-us-east-2-171683036970')
                    hcpm.upload_file(localfile, localfile)
                    filespath = 'https://elasticbeanstalk-us-east-2-171683036970.s3.us-east-2.amazonaws.com/' + localfile
                    update = NameSpaces.objects.get(uuid=instance.uuid)
                    print(update)
                    update.fileurl = filespath
                    # update.uuid = uuid.uuid4()
                    update.save()
                    # print('sea id', NameSpaces.objects.filter(serializers.data))
                    return Response(status='200')
                else:
                    print('user is not active')
                    return JsonResponse({'Message': 'User not allowed to upload file'})
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CreateTenants(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TenantsSerializer
    parser_classes = (FormParser, MultiPartParser)


class CreateRegions(generics.CreateAPIView):
    serializer_class = RegionSerializer
    parser_classes = (FormParser, MultiPartParser)
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

# class NameSpaces(viewsets.ModelViewSet):
# 	authentication_classes = [SessionAuthentication, BasicAuthentication]
# 	permission_classes = [IsAuthenticated]
# 	queryset = NameSpaces.objects.all()
# 	serializer_class = NameSpacesSerializer
