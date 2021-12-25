from django import forms
from django.forms import ModelForm
from .models import *

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'place', 'eventtype', 'date', 'description')
		labels = {
        'name': '',
        'place': 'Event Place',
        'eventtype': 'Event Type',
        'date':'DD-MM-YYYY',
		'description': '',
		'manager': 'Manager',

		}

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'place': forms.Select(attrs={'class':'form-control', 'placeholder':'Event City'}),
			'eventtype': forms.Select(attrs={'class':'form-select', 'placeholder':'Event Type'}),
			'date': forms.TextInput(attrs={'class':'form-select', 'placeholder':'Event Date'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
			'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
		}