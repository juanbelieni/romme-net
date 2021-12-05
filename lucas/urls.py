import django.urls as urls
from . import views

urlpatterns = [
    urls.path("", views.analysis, name="analysis-lucas"),
]
