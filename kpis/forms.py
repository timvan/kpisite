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