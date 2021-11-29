from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ProviderForm
from .models import Provider

# View: list
# Description: list all providers
def provider_list(request):
    providers = Provider.objects.order_by("id")
    return render(request, "provider/list.html", {"providers": providers})


# View: create
# Description: create a new provider
def provider_create(request):
    if request.method == "POST":
        form = ProviderForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            provider = Provider(
                name=data["name"],
                phone=data["phone"],
                address=data["address"],
            )

            provider.save()

            return HttpResponseRedirect(reverse("provider-list"))

    else:
        form = ProviderForm()

    return render(request, "provider/create.html", {"form": form})


# View: update
# Description: update a provider
def provider_update(request, id):
    if request.method == "POST":
        form = ProviderForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            provider = Provider.objects.get(id=id)

            provider.name = data["name"]
            provider.phone = data["phone"]
            provider.address = data["address"]

            provider.save()

            return HttpResponseRedirect(reverse("provider-list"))

    else:
        provider = Provider.objects.get(id=id)
        form = ProviderForm(
            initial={
                "name": provider.name,
                "phone": provider.phone,
                "address": provider.address,
            }
        )

    return render(request, "provider/update.html", {"id": id, "form": form})


# View: delete
# Description: delete a provider
def provider_delete(request, id):
    provider = Provider.objects.get(id=id)
    provider.delete()

    return HttpResponseRedirect(reverse("provider-list"))
