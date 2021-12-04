import django.urls as urls
from . import views

urlpatterns = [
    urls.path("", views.dashboard, name="dashboard"),
    urls.path('relatorio_gastos', views.relatorio_gastos, name="relatorio_gastos"),
]