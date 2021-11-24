from django.shortcuts import render

# View: list
# Description: list all providers
def provider_list(request):
    return render(request, "provider/list.html")

# View: create
# Description: create a new provider
def provider_create(request):
    return render(request, "provider/create.html")