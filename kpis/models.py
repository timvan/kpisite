from django.db import models
from django.utils import timezone
from django.db.models import Sum

# Create your models here.

class KPI(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	date_created = models.DateTimeField(default = timezone.now)
	units = models.CharField(max_length = 20)

	def __str__(self):
		return self.title

	def get_total(self):
		activity_list = activity.objects.filter(kpi_id = self.id)
		self.total = activity_list.aggregate(Sum('activity_value'))['activity_value__sum']
		return self.total

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

	RED = 'RD'
	GREEN = 'GR'
	BLUE = 'BL'

	group_choices = (
		(RED, 'red'),
		(GREEN, 'green'),
		(BLUE, 'blue'),
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



	# icon_choices = {
	# 	"XXX" : "XXXX",
	# }
	# icon = models.ChoiceField(group_choice, defaul ="XXXX")

class activity(models.Model):
	activity_value = models.IntegerField(default = 1) # possibly default = 1,
	kpi = models.ForeignKey(KPI, on_delete = models.CASCADE, parent_link = True)
	date_time = models.DateTimeField(default = timezone.now)
