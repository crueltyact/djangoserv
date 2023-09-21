from template.serializers import TemplateSerializer
from template.models import Template
from rest_framework.viewsets import ModelViewSet



class TemplateViewSet(ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    

