from rest_framework import serializers
from themes.models import Theme

class ThemesSerializers(serializers.Serializer):
    class Meta:
        model = Theme
        fields = '__all__'