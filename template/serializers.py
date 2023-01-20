from rest_framework import serializers
from template.models import Template

class TemplateSerializer(serializers.Serializer):
    class Meta:
        model = Template
        fields = ('__all__')