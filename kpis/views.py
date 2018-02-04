from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import KPI, Activity
from .forms import KpiForm

# Create your views here.

def landing_page(request):
	#return HttpResponse("hello world, it's the landing_page")
	return render(request, 'kpis/landing_page.html')


#-------------- KPI Actions -------------#

@login_required
def index(request):

	kpi_list = KPI.objects.filter(author = request.user).order_by('date_created')

	context = {
		'kpi_list' : kpi_list,
	}
	return render(request, 'kpis/index.html', context)

@login_required
def kpi_detail(request, pk):
	kpi = get_object_or_404(KPI, pk = pk)
	activity_list = Activity.objects.filter(kpi_id = kpi.id).order_by('-datetime_logged')
	context = {
		'kpi' : kpi,
		'activity_list' : activity_list
	}
	return render(request, 'kpis/kpi_detail.html', context)


@login_required
def kpi_new(request):
	if request.method == "POST":
		form = KpiForm(request.POST)
		if form.is_valid():
			kpi = form.save(commit = False)
			kpi.author = request.user
			kpi.save()
			return redirect('index')
	else:
		form = KpiForm()
	return render(request, 'kpis/kpi_new.html', {'form' : form})

@login_required
def kpi_edit(request, pk):
	kpi = get_object_or_404(KPI, pk = pk)
	if request.method == "POST":
		form = KpiForm(request.POST, instance = kpi)
		if form.is_valid():
			kpi = form.save(commit = False)
			kpi.author = request.user
			kpi.save()
			return redirect('kpi_detail', pk = kpi.pk)
	else:
		form = KpiForm(instance = kpi)

	context = {
		'form' : form,
		'kpi' : kpi,
	}

	return render(request, 'kpis/kpi_edit.html', context)



#-------------- Activity Actions -------------#

def activity_delete(request, pk, pk_act):
	 activity = get_object_or_404(Activity, pk = pk_act)
	 activity.delete()
	 return redirect('kpi_detail', pk = pk)

#-------------- Administration -------------#

@login_required
def log_activity(response, pk):
	kpi = get_object_or_404(KPI, pk = pk)
	new_activity = Activity(kpi = kpi)
	new_activity.save()
	return redirect('index')


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username = username, password = raw_password)
			if user is not None:
				login(request, user)	
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signup.html', {'form': form})
