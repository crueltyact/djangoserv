from rest_framework import serializers
from project_id.models import MyProject

class MyProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProject
        fields = '__all__'