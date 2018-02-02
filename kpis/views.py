from django.shortcuts import render
from django.http import HttpResponse

from .models import KPI, activity

# Create your views here.

def index(request):

	kpi_list = KPI.objects.filter(author = request.user).order_by('date_created')

	context = {
		'kpi_list' : kpi_list,
	}
	return render(request, 'kpis/index.html', context)


