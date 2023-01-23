from themes.models import Theme
from themes.serializers import ThemeSerializer




from rest_framework.viewsets import ModelViewSet

class ThemeViewSet(ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

# Create your views here.
