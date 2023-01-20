from rest_framework.routers import SimpleRouter
from template.views import TemplateViewSet

router = SimpleRouter()

router.register(r'templates', TemplateViewSet, basename='templates')