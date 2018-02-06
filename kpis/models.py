from django.db import models
from django.utils import timezone
from django.db.models import Sum
from datetime import date, datetime, timedelta

# Create your models here.

class KPI(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	date_created = models.DateTimeField(default = timezone.now)
	units = models.CharField(max_length = 20)

	# Defining Periodicy

	DAILY = 'DY'
	WEEKLY = 'WK'
	MONTHLY = 'MH'
	YEARLY = 'YR'

	periodicity_choices = {
		(DAILY, 'Daily'),
		(WEEKLY, 'Weekly'),
		(MONTHLY, 'Monthly'),
		(YEARLY, 'Yearly'),
	}

	periodicity = models.CharField(
		max_length = 2,
		choices = periodicity_choices,
		default = DAILY,
		)

	def get_periodicity(self):

		periodicity_written_choices = {
			'DY' : 'Today',
			'WK' : 'Week',
			'MH' : 'Month',
			'YR' : 'Year',
		}

		periodicity_written = periodicity_written_choices[self.periodicity]

		return periodicity_written



	# Defining Group colours

	RED = 'RD'
	GREEN = 'GR'
	BLUE = 'BL'

	group_choices = (
		(RED, 'Red'),
		(GREEN, 'Green'),
		(BLUE, 'Blue'),
	)

	group = models.CharField(
		max_length = 2,
		choices = group_choices,
		default = BLUE,
	)

	def get_group_color(self):

		group_css_colors = {
			'RD' : '#d9534f',
			'GR' : '#5cb85c',
			'BL' : '#337ab7',
		}

		self.color = group_css_colors[self.group]
		return self.color


	def __str__(self):
		return self.title


	def get_all_activities_this_period(self):

		datetime_now = timezone.now()
		tzinfo = datetime_now.tzinfo

		year = datetime_now.year
		month = datetime_now.month
		day = datetime_now.day

		weekday = datetime_now.weekday()
		
		date_ranges = {
			'DY' : datetime(year, month, day, tzinfo = tzinfo),
			'WK' : datetime(year, month, day,  tzinfo = tzinfo) - timedelta(weekday),
			'MH' : datetime(year, month, 1,  tzinfo = tzinfo),
			'YR' : datetime(year, 1, 1,  tzinfo = tzinfo),

		}


		activity_list = Activity.objects.filter(kpi_id = self.id)
		activity_list = activity_list.filter(datetime_logged__gte = date_ranges[self.periodicity],
			datetime_logged__lt = datetime_now
			)

		return activity_list



	def get_period_total(self):

		activity_list = self.get_all_activities_this_period()
		period_total = activity_list.aggregate(Sum('activity_value'))['activity_value__sum']

		if period_total == None:
			return 0
		else:
			return period_total

		print(period_total)


	"""
	

	def get_total(self):
		activity_list = Activity.objects.filter(kpi_id = self.id)
		self.total = activity_list.aggregate(Sum('activity_value'))['activity_value__sum']
		
		return self.total


		if self.total == None:
			return 0
		else:
			return self.total
	
	def get_daily_total(self):

		today = date.today()

		activity_list = Activity.objects.filter(kpi_id = self.id)

		activity_list = activity_list.filter(datetime_logged__year=today.year, 
			datetime_logged__month=today.month, 
			datetime_logged__day=today.day)

		self.daily_total = activity_list.aggregate(Sum('activity_value'))['activity_value__sum']

		if self.daily_total == None:
			return 0
		else:
			return self.daily_total

	"""





	## Granularity to be designed. I.e group taget/entries per day/week/5days
	# gran_choices = {
	# 	"XXX" : "XXX"
	# }
	# granularity = models.ChoiceField(gran_choices, default = "days")

	## Targets to designed upon copletion of granularity
	# target = models.IntegerField(default = 0)
	# target_units = models.Field(max_length = 25)	


	##  Additional catgorisation and customisation

	# category = models.CharField(max_length = 25)

	# icon_choices = {
	# 	"XXX" : "XXXX",
	# }
	# icon = models.ChoiceField(group_choice, defaul ="XXXX")

class Activity(models.Model):
	activity_value = models.IntegerField(default = 1) # possibly default = 1,
	kpi = models.ForeignKey(KPI, on_delete = models.CASCADE, parent_link = True)
	datetime_logged = models.DateTimeField(default = timezone.now)
