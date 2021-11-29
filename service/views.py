from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ServiceForm
from .models import Service

# View: list
# Description: list all services
def service_list(request):
    services = Service.objects.order_by("id")
    return render(request, "service/list.html", {"services": services})


# View: create
# Description: create a new service
def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            service = Service(
                name=data["name"],
            )

            service.save()

            return HttpResponseRedirect(reverse("service-list"))

    else:
        form = ServiceForm()

    return render(request, "service/create.html", {"form": form})


# View: update
# Description: update a service
def service_update(request, id):
    if request.method == "POST":
        form = ServiceForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            service = Service.objects.get(id=id)

            service.name = data["name"]

            service.save()

            return HttpResponseRedirect(reverse("service-list"))

    else:
        service = Service.objects.get(id=id)
        form = ServiceForm(
            initial={
                "name": service.name,
            }
        )

    return render(request, "service/update.html", {"id": id, "form": form})


# View: delete
# Description: delete a service
def service_delete(request, id):
    service = Service.objects.get(id=id)
    service.delete()

    return HttpResponseRedirect(reverse("service-list"))
