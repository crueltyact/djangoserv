from rest_framework import serializers
from project.models import Project
from project_id.models import MyProject
from themes.models import Theme

class ThemeSerializerForProject(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['shortdesc']

class MyProjectSerializerForProject(serializers.ModelSerializer):
    class Meta:
        model = MyProject
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    theme_data = ThemeSerializerForProject(source = 'themes', many = True)
    project_data = MyProjectSerializerForProject(source = 'project_id', many = True)
    class Meta:
        model = Project
        exclude = ['themes', 'project_id']