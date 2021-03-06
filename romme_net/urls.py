"""romme_net URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    # Dashboard view, at '/',
    path("", include("dashboard.urls")),
    # Provider views
    path("prestadores/", include("provider.urls")),
    # Service views
    path("servicos/", include("service.urls")),
    # Material views
    path("materiais/", include("material.urls")),
    # Machine views
    path("maquinas/", include("machine.urls")),
    # Occurrence views
    path("ocorrencias/", include("occurrence.urls")),
    # Analysis views
    path("analises/", views.analysis, name="analysis"),
    path("analises/juan/", include("juan.urls")),
    path("analises/lucas/", include("lucas.urls")),
    path("analises/nicole/", include("nicole.urls")),
    path("analises/carlos/", include("carlos.urls")),
    # Static files
    *staticfiles_urlpatterns(),
]
