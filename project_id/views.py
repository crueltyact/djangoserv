from project_id.serializers import MyProjectSerializer
from project_id.models import MyProject  
from rest_framework.viewsets import ModelViewSet

class MyProjectViewSet(ModelViewSet):
    queryset = MyProject .objects.all()
    serializer_class = MyProjectSerializer


# Create your views here.
