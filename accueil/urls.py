from django.urls import path, include

from . import views
import accueil

app_name = 'accueil'

urlpatterns = [
        path('', views.accueil, name=accueil)
]