import django.urls as urls
from . import views

urlpatterns = [
    urls.path("", views.provider_list, name="provider-list"),
    urls.path("novo/", views.provider_create, name="provider-create"),
]
