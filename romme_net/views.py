from django.http import HttpResponse
from django.template import loader

# View: dashboard
# Description: renders the dashboard page
def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())
