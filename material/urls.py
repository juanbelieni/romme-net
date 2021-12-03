import django.urls as urls
from . import views

urlpatterns = [
    urls.path("", views.material_list, name="material-list"),
    urls.path("novo/", views.material_create, name="material-create"),
    urls.path("editar/<int:id>/", views.material_update, name="material-update"),
    urls.path("remover/<int:id>/", views.material_delete, name="material-delete"),
]
