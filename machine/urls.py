import django.urls as urls
from . import views

urlpatterns = [
    urls.path("", views.machine_list, name="machine-list"),
    urls.path("novo/", views.machine_create, name="machine-create"),
    urls.path("editar/<int:id>/", views.machine_update, name="machine-update"),
    urls.path("remover/<int:id>/", views.machine_delete, name="machine-delete"),
]
