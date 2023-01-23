from project.serializers import ProjectSerializer
from project.models import Project  
from rest_framework.viewsets import ModelViewSet

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer