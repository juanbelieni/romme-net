import django.urls as urls
from . import views

urlpatterns = [
    urls.path("", views.service_list, name="service-list"),
    urls.path("novo/", views.service_create, name="service-create"),
    urls.path("editar/<int:id>/", views.service_update, name="service-update"),
    urls.path("remover/<int:id>/", views.service_delete, name="service-delete"),
]
