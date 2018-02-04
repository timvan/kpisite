from django import forms

from .models import KPI

class NewKpiForm(forms.ModelForm):

	class Meta:
		model = KPI
		fields = ('title', 'units', 'group')