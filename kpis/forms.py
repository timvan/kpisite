from django import forms

from .models import KPI

class KpiForm(forms.ModelForm):

	class Meta:
		model = KPI
		fields = ('title', 'group', 'periodicity')