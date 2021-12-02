from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import MaterialForm
from .models import Material

# View: list
# Description: list all material
def material_list(request):
    materials = Material.objects.order_by("id")
    return render(request, "material/list.html", {"materials": materials})


# View: create
# Description: create a new material
def material_create(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            material = Material(
                name=data["name"],
                category=data["category"],
            )
            
            material.save()

            return HttpResponseRedirect(reverse("material-list"))

    else:
        form = MaterialForm()

    return render(request, "material/create.html", {"form": form})


# View: update
# Description: update a material
def material_update(request, id):
    if request.method == "POST":
        form = MaterialForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            material = Material.objects.get(id=id)

            material.name = data["name"]
            material.category=data["category"]

            material.save()

            return HttpResponseRedirect(reverse("material-list"))

    else:
        material = Material.objects.get(id=id)
        form = MaterialForm(
            initial={
                "name": material.name,
                "category": material.category
            }
        )

    return render(request, "material/update.html", {"id": id, "form": form})


# View: delete
# Description: delete a material
def material_delete(request, id):
    material = Material.objects.get(id=id)
    material.delete()

    return HttpResponseRedirect(reverse("material-list"))
