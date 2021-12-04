import django.urls as urls
from . import views

urlpatterns = [
    urls.path("", views.dashboard, name="dashboard"),
    urls.path('relatorio_gastos', views.relatorio_gastos, name="relatorio_gastos"),
    urls.path('retorna_total_gasto', views.retorna_total_gasto, name="retorna_total_gasto"),
    urls.path('retorna_ocorrencias_mes', views.retorna_ocorrencias_mes, name="retorna_ocorrencias_mes"),
    urls.path('retorna_ocorrencias_semana', views.retorna_ocorrencias_semana, name="retorna_ocorrencias_semana"),
    urls.path('retorna_ocorrencias_hoje', views.retorna_ocorrencias_hoje, name="retorna_ocorrencias_hoje"),
]
