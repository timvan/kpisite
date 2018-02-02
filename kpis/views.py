from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import KPI, activity

# Create your views here.

def index(request):

	kpi_list = KPI.objects.filter(author = request.user).order_by('date_created')

	context = {
		'kpi_list' : kpi_list,
	}
	return render(request, 'kpis/index.html', context)


def log_activity(response, pk):
	kpi = get_object_or_404(KPI, pk = pk)
	new_activity = activity(kpi = kpi)
	new_activity.save()
	return redirect('index')