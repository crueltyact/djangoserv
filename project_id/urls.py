from django.urls import path
from project_id.views import MyProject_list

urlpatterns = [
    path('project_id', MyProject_list)
]