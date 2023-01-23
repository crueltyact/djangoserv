from rest_framework import serializers
from themes.models import Theme
from template.models import Template

class TemplateSerializerForTheme(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['name']

class ThemeSerializer(serializers.ModelSerializer):
    template_data = TemplateSerializerForTheme(source='template', many = True)
    class Meta:
        model = Theme
        exclude = ['template']