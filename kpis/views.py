from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.db.models import Sum
from django.core.paginator import Paginator
from django.views.generic import DetailView

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import KPI, Activity
from .forms import KpiForm, ActivityForm

from datetime import date, datetime, timedelta
import csv
import random
import json



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
	activity_list = Activity.objects.filter(kpi = kpi).order_by('-datetime_logged')
	paginator = Paginator(activity_list, 10)
	page = request.GET.get('page')
	activities = paginator.get_page(page)

	context = {
		'kpi' : kpi,
		'activity_list' : activities,
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
def kpi_delete(request, pk):
	kpi = get_object_or_404(KPI, pk = pk)
	kpi.delete()
	return redirect('index')

@login_required
def kpi_edit(request, pk):
	kpi = get_object_or_404(KPI, pk = pk)
	print("POST: ", request.POST)
	if request.method == "POST":
		form = KpiForm(request.POST, instance = kpi)
		if form.is_valid():
			print("form is valid")
			print(form)
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


@login_required
def log_activity(response, pk):
	kpi = get_object_or_404(KPI, pk = pk)
	new_activity = Activity(kpi = kpi)
	new_activity.save()
	return redirect('index')


#-------------- Create Example Data -------------#
	
def create_examples(request):
	kpi_titles = ["Coffees", "Swum in the Sea", "Went surfing", "Hours worked on project", "Km's ran", "Films watched"]
	kpi_periodicities = ['WK', 'MH', 'MH', "DY", "WK", "YR"]
	kpi_groups = ["RD", "BL", "BL", "GR", "BL", "RD"]
	kpi_units = "times"

	activity_amount_max = [2, 1, 1, 10, 15, 1]

	today = datetime.today()

	for i in range(len(kpi_titles)):
		kpi = KPI(author = request.user, title = kpi_titles[i], units = kpi_units, periodicity = kpi_periodicities[i], group = kpi_groups[i])
		kpi.save()
		for j in range(random.randint(20, 300)):
			new_activity = Activity(kpi = kpi, activity_value = random.randint(1,activity_amount_max[i]), datetime_logged = today - timedelta(random.randint(0, 365)))
			new_activity.save()

	return redirect('index')



#-------------- Activity Actions -------------#

def kpi_datatable(request, pk):
	kpi = get_object_or_404(KPI, pk = pk)
	activity_list = Activity.objects.filter(kpi = kpi).order_by('-datetime_logged')
	paginator = Paginator(activity_list, 10)
	page = request.GET.get('page')
	activities = paginator.get_page(page)
	context = {
		'kpi' : kpi,
		'activity_list' : activities,
	}
	return render(request, 'kpis/kpi_datatable.html', context)


def activity_delete(request, pk, pk_act):
	activity = get_object_or_404(Activity, pk = pk_act)
	activity.delete()
	print(request)
	return redirect('kpi_datatable', pk = pk)


def activity_edit(request, pk, pk_act):
	# print('views.activity_edit', pk, pk_act)
	kpi = get_object_or_404(KPI, pk = pk)
	activity = get_object_or_404(Activity, pk = pk_act)

	response_data = {}

	if request.method == "POST":
		form = ActivityForm(request.POST, instance = activity)

		# NEED TO ADD - detection of dates great than current date

		if form.is_valid():

			activity = form.save(commit = False)
			activity.save()

			response_data['result'] = 'Succes'
			response_data['activity'] = activity.pk
			response_data['kpi'] = activity.kpi.pk.__str__()
			response_data['datetime_logged'] = activity.datetime_logged.__str__()
			response_data['activity_value'] = activity.activity_value

			return HttpResponse(
				json.dumps(response_data),
				content_type = "application/json"
				)

		else:
			response_data['result'] = 'Form not valid'

	else:
		return HttpResponse(
			json.dumps({"error" : "nothing happening"}),
			content_type = "application/json"
			)


#-------------- Administration -------------#


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


#-------------- Export CSV -------------#

def export_csv(request):
	#today = date.today()
	#filename = "_".join(["KPIsExport", str(request.user), str(today.year), str(today.month), str(today.day)]) + ".csv"
	#print (filename)
	response = HttpResponse(content_type = 'text/csv')
	response['Content-Disposition'] = 'attachement; filename-"export.csv"'

	writer = csv.writer(response)
	writer.writerow(['KPI', 'DateTime', 'Activity'])
	kpi_list = KPI.objects.filter(author = request.user)
	for kpi in kpi_list:
		activity_list = Activity.objects.filter(kpi_id = kpi.id)
		for activity in activity_list:
			writer.writerow([kpi.title, activity.datetime_logged, activity.activity_value])

	return response


#-------------- Charts -------------#

def kpi_charts(request, pk):
	kpi = get_object_or_404(KPI, pk = pk)
	context = {
		'kpi' : kpi,
	}
	return render(request, 'kpis/kpi_charts.html', context)


class ChartWeekDays(APIView):
	authentication_classes = []
	permission_classes = []
	def get(self, request, pk, format=None):

		kpi = get_object_or_404(KPI, pk = pk)
		activity_list = Activity.objects.filter(kpi_id = kpi.id)
		labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

		chart_data = []

		for i in [2, 3, 4, 5, 6, 7, 1]:
			query = Activity.objects.filter(kpi_id = kpi.id).filter(datetime_logged__week_day=i)
			query_total = query.aggregate(Sum('activity_value'))['activity_value__sum']
			chart_data.append(query_total)

		print(chart_data)

		data = {
			"chart_data" : chart_data,
			"chart_labels" : labels,
		}
		return Response(data)

class ChartHistory(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, pk, format=None):

		kpi = get_object_or_404(KPI, pk = pk)
		activity_list = Activity.objects.filter(kpi_id = kpi.id)
		labels_monthly = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

		chart_data = []
		labels = []

		now = datetime.now()

		start_date = now
		end_date = datetime(now.year, now.month, 1)

		for i in range(1,13):
			query = Activity.objects.filter(kpi_id = kpi.id)
			query_activities = query.filter(datetime_logged__lte = start_date).filter(datetime_logged__gte =  end_date)
			query_total = query_activities.aggregate(Sum('activity_value'))['activity_value__sum']
			chart_data.append(query_total)

			if start_date.month == 1:
				labels.append(labels_monthly[start_date.month - 1] + " " + str(start_date.year))
			else:
				labels.append(labels_monthly[start_date.month - 1])

			start_date = end_date - timedelta(microseconds = 1)
			if (12 + now.month - i) % 12 == 0:
				end_date = datetime(end_date.year - 1, 12, 1)
			else:
				end_date = datetime(end_date.year, (12 + end_date.month - 1) % 12, 1)

		print(chart_data)

		data = {
			"chart_data" : chart_data[::-1],
			"chart_labels" : labels[::-1],
		}
		return Response(data)





