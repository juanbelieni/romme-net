from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import MachinesForm
from .models import Machines

# View: list
# Description: list all machines
def machines_list(request):
    machines = Machines.objects.order_by("id")
    return render(request, "machines/list.html", {"machines": machines})


# View: create
# Description: create a new machine
def machines_create(request):
    if request.method == "POST":
        form = MachinesForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            machine = Machines(
                name=data["name"],
                description=data["description"],
            )

            machine.save()

            return HttpResponseRedirect(reverse("machines-list"))

    else:
        form = MachinesForm()

    return render(request, "machines/create.html", {"form": form})


# View: update
# Description: update a machine
def machines_update(request, id):
    if request.method == "POST":
        form = MachinesForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            machine = Machines.objects.get(id=id)

            machine.name = data["name"]
            machine.description=data["description"]

            machine.save()

            return HttpResponseRedirect(reverse("machines-list"))

    else:
        machine = Machines.objects.get(id=id)
        form = MachinesForm(
            initial={
                "name": machine.name,
                "description": machine.description
            }
        )

    return render(request, "machines/update.html", {"id": id, "form": form})


# View: delete
# Description: delete a machine
def machines_delete(request, id):
    machine = Machines.objects.get(id=id)
    machine.delete()

    return HttpResponseRedirect(reverse("machines-list"))
