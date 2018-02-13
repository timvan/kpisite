from django import forms

from .models import KPI, Activity

class KpiForm(forms.ModelForm):

	class Meta:
		model = KPI
		fields = ('title', 'group', 'periodicity', 'date_created')


class ActivityForm(forms.ModelForm):

	class Meta:
		model = Activity
		fields = ('datetime_logged', 'activity_value')

		widgets = {
			'datetime_logged' : forms.DateTimeInput(attrs={
				'id': 'id_datetime_logged',
				'required' : True,
				}),
			'activity_value' : forms.NumberInput(attrs={
				'id': 'id_activity_value',
				'required' : True
				}),
		}