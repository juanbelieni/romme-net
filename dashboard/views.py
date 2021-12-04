from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from occurrence.models import Occurrence

def dashboard(request):
    return render(request, "dashboard.html")

def relatorio_gastos(request):
    x = Occurrence.objects.all()
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    mes = datetime.now().month + 1
    ano = datetime.now().year
    y = []
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.total_cost for i in x if i.datetime.month == mes and i.datetime.year == ano])

        data.append(y)
        labels.append(meses[mes-1])

    data_json = {'data': data[::-1], 'labels': labels[::-1]}
     
    return JsonResponse(data_json)