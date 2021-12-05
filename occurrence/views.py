from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from material.models import Material
from occurrence.models import (
    Occurrence,
    OccurrenceCategory,
    OccurrenceMaterial,
    OccurrenceService,
)
from machine.models import Machine
from service.models import Service
from provider.models import Provider
from django.urls import reverse

# View: list
# Description: list all occurrences
def occurrence_list(request):
    occurrences = Occurrence.objects.order_by("-datetime").select_related("machine")
    return render(request, "occurrence/list.html", {"occurrences": occurrences})


# View: create
# Description: create a new occurrence
def occurrence_create(request):
    if request.method == "POST":
        description = request.POST.get("description")
        category = request.POST.get("category")
        machine_id = request.POST.get("machine")
        downtime = request.POST.get("downtime")
        total_cost = request.POST.get("total_cost")
        datetime = request.POST.get("datetime")

        machine = Machine.objects.get(id=machine_id)
        occurrence = Occurrence(
            description=description,
            total_cost=total_cost,
            category=category,
            machine=machine,
            downtime=downtime,
            datetime=datetime,
        )

        occurrence.save()

        services_id = request.POST.getlist("os_services")
        providers_id = request.POST.getlist("os_providers")

        for service_id, provider_id in zip(services_id, providers_id):
            service = Service.objects.get(id=service_id)
            provider = Provider.objects.get(id=provider_id)

            occurrence_service = OccurrenceService(
                occurrence=occurrence,
                service=service,
                provider=provider,
            )

            occurrence_service.save()

        materials_id = request.POST.getlist("om_materials")
        quantities = request.POST.getlist("om_quantities")

        for material_id, quantity in zip(materials_id, quantities):
            material = Material.objects.get(id=material_id)

            occurrence_material = OccurrenceMaterial(
                occurrence=occurrence,
                material=material,
                quantity=quantity,
            )

            occurrence_material.save()

        return HttpResponseRedirect(reverse("occurrence-list"))

    categories = OccurrenceCategory.choices
    machines = Machine.objects.all()
    services = Service.objects.all()
    providers = Provider.objects.all()
    materials = Material.objects.all()

    params = {
        "categories": categories,
        "machines": machines,
        "services": services,
        "providers": providers,
        "materials": materials,
    }

    return render(request, "occurrence/create.html", params)
