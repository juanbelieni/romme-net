from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import JsonResponse
from occurrence.models import Occurrence
from django.db.models import Sum

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

def retorna_total_gasto(request):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=30)
    

    x = Occurrence.objects.filter(datetime__range=[startdate, enddate])
    total = x.aggregate(Sum('total_cost'))['total_cost__sum']
    return JsonResponse({'total': total})

def retorna_ocorrencias_mes(request):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=30)
    

    x = Occurrence.objects.filter(datetime__range=[startdate, enddate])
    total = x.count()
    return JsonResponse({'total': total})

def retorna_ocorrencias_semana(request):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=7)

    x = Occurrence.objects.filter(datetime__range=[startdate, enddate])
    total = x.count()
    return JsonResponse({'total': total})

""" def retorna_ocorrencias_hoje(request):
    enddate = datetime.today()
    startdate = enddate - timedelta(hours=24)

    x = Occurrence.objects.filter(datetime__range=[startdate, enddate])
    total = x.count()
    return JsonResponse({'total': total}) """

def retorna_ocorrencias_hoje(request):
    mes = datetime.now().month
    ano = datetime.now().year 
    dia = datetime.now().day

    x = Occurrence.objects.filter(datetime__year=ano, 
                      datetime__month=mes, datetime__day = dia)
    total = x.count()
    return JsonResponse({'total': total})