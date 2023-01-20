from django.core import serializers
from project_id.models import MyProject
from django.http import JsonResponse
from rest_framework.response import Response

def MyProject_list(request):
    MyProjects = MyProject.objects.all()
    data = serializers.serialize("json", MyProjects)
    return JsonResponse(data={'data':data})

# Create your views here.
