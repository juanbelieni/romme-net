import django.urls as urls
from . import views

urlpatterns = [
    urls.path("", views.machines_list, name="machines-list"),
    urls.path("novo/", views.machines_create, name="machines-create"),
    urls.path("editar/<int:id>/", views.machines_update, name="machines-update"),
    urls.path("remover/<int:id>/", views.machines_delete, name="machines-delete"),
]
