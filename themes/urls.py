from django.urls import path
from themes.views import themes_list

urlpatterns = [
    path('themes', themes_list)
]
