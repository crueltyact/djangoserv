from rest_framework.routers import SimpleRouter
from template.views import TemplateViewSet
from themes.views import ThemeViewSet
from reviews.views import ReviewViewSet
from project_id.views import MyProjectViewSet
from project.views import ProjectViewSet
from authentif.views import UserViewSet

router = SimpleRouter()

router.register(r'templates', TemplateViewSet)
router.register(r'themes', ThemeViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'project', MyProjectViewSet)
router.register(r'myprojects', ProjectViewSet)
router.register(r'auth', UserViewSet)
