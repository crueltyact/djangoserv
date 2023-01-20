from django.core import serializers
from themes.models import Theme
from rest_framework.response import Response
from rest_framework.decorators import api_view
from themes.serializers import ThemesSerializers

@api_view()
def themes_list(request):
    themes = Theme.objects.all()
    data = ThemesSerializers(instance=themes, many=True).data
    return Response(data={'data':data})

# Create your views here.
