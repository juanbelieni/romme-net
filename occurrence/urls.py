import django.urls as urls
from . import views

urlpatterns = [
    urls.path("", views.occurrence_list, name="occurrence-list"),
    urls.path("novo/", views.occurrence_create, name="occurrence-create"),
    # urls.path("editar/<int:id>/", views.machine_update, name="machine-update"),
    # urls.path("remover/<int:id>/", views.machine_delete, name="machine-delete"),
]
