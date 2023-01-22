# from django.core import serializers
# from template.models import Template
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from template.serializers import TemplateSerializer
# from template.models import Template

# @api_view()
# def template_list(request):
#     template = Template.objects.all()
#     data = TemplateSerializer(instance=template, many=True).data
#     return Response(data={'data': data})

# Create your views here.


# попытка 2
from template.serializers import TemplateSerializer
from template.models import Template
from rest_framework.viewsets import ModelViewSet

class TemplateViewSet(ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

# попытка 3
# from template.serializers import TemplateSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from themes.models import Template
# from django.forms import model_to_dict


# class templateAPIView(APIView):
#     def get(self, request):
#         lst = Template.objects.all().values()
#         return Response({'posts':list(lst)})

    # def post(self, request):
    #     post_new = Template.objects.create(
    #         name = request.data['name'],
    #         desc = request.data['desc'],
    #         cover = request.data['cover'],
    #     )

    #     return Response({'post': model_to_dict(post_new)})

# popitka 4

# from django.http import JsonResponse
# from template.models import Template
# from django.forms.models import model_to_dict

# def ViewTemplate(request, *args, **kwargs):
#     model_data = Template.objects.all()
#     data ={}
#     if model_data:
#         data = model_to_dict(model_data, fields="__all__")

#     return JsonResponse(data)

# poptka 5

# from django.http import JsonResponse
# from template.models import Template
# from template.serializers import TemplateSerializer

# def ViewTemplate(request):
#     data = Template.objects.all()
#     serializer = TemplateSerializer(data, many=True)
#     return JsonResponse(serializer.data)