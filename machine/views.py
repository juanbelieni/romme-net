from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import MachineForm
from .models import Machine

# View: list
# Description: list all machines
def machine_list(request):
    machines = Machine.objects.order_by("id")
    return render(request, "machine/list.html", {"machines": machines})


# View: create
# Description: create a new machine
def machine_create(request):
    if request.method == "POST":
        form = MachineForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            machine = Machine(
                name=data["name"],
                description=data["description"],
            )

            machine.save()

            return HttpResponseRedirect(reverse("machine-list"))

    else:
        form = MachineForm()

    return render(request, "machine/create.html", {"form": form})


# View: update
# Description: update a machine
def machine_update(request, id):
    if request.method == "POST":
        form = MachineForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            machine = Machine.objects.get(id=id)

            machine.name = data["name"]
            machine.description=data["description"]

            machine.save()

            return HttpResponseRedirect(reverse("machine-list"))

    else:
        machine = Machine.objects.get(id=id)
        form = MachineForm(
            initial={
                "name": machine.name,
                "description": machine.description
            }
        )

    return render(request, "machine/update.html", {"id": id, "form": form})


# View: delete
# Description: delete a machine
def machine_delete(request, id):
    machine = Machine.objects.get(id=id)
    machine.delete()

    return HttpResponseRedirect(reverse("machine-list"))
