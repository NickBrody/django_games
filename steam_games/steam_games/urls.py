"""
URL configuration for steam_games project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from add_note_on_site.views import game_autocomplete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='add_note_on_site/index.html')),
    path('add/', include('add_note_on_site.urls')),
    path('auth/', include('my_auth.urls')),
    path('game-autocomplete/', game_autocomplete, name='game-autocomplete'),
    
]
