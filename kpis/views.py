from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import KPI, activity

# Create your views here.

def landing_page(request):
	#return HttpResponse("hello world, it's the landing_page")
	return render(request, 'kpis/landing_page.html')

@login_required
def index(request):

	kpi_list = KPI.objects.filter(author = request.user).order_by('date_created')

	context = {
		'kpi_list' : kpi_list,
	}
	return render(request, 'kpis/index.html', context)

@login_required
def log_activity(response, pk):
	kpi = get_object_or_404(KPI, pk = pk)
	new_activity = activity(kpi = kpi)
	new_activity.save()
	return redirect('index')

@login_required
def detail(response, pk):
	return HttpResponse("Hello World")

