from django import forms

from .models import KPI, Activity

class KpiForm(forms.ModelForm):

	class Meta:
		model = KPI
		fields = ('title', 'group', 'periodicity')


class ActivityForm(forms.ModelForm):

	class Meta:
		model = Activity
		fields = ('datetime_logged', 'activity_value')

		widgets = {
			'datetime_logged' : forms.TextInput(attrs={
				'id': 'post-datetime_logged',
				'required' : True,
				'placeholder' : "date 2"
				}),
			'activity_value' : forms.TextInput(attrs={
				'id': 'post-activity_value',
				'required' : True,
				'placeholder' : "activity 2"
				}),
		}