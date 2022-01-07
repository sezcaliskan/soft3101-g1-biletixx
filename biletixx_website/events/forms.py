from django import forms
from django.forms import ModelForm
from .models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'place', 'eventtype', 'date', 'description','venue','hour','price','max_sellable_tickets')
		labels = {
        'name': '',
        'place': 'Event Place',
        'eventtype': 'Event Type',
        'date':'DD-MM-YYYY',
		'description': '',
		'venue': 'Event Venue',
		'hour': 'Event Hour',
		'price': 'Event Price',
		'max_sellable_tickets': 'Max Sellable Tickets',
		'manager': 'Manager',


		}

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'place': forms.Select(attrs={'class':'form-control', 'placeholder':'Event City'}),
			'eventtype': forms.Select(attrs={'class':'form-select', 'placeholder':'Event Type'}),
			#'date': forms.TextInput(attrs={'class':'form-select', 'placeholder':'Event Date'}),
			'date': DateInput(),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
			'venue': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Venue'}),
			'hour': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Hour'}),
			'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Price'}),
			'max_sellable_tickets': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Max Sellable Tickets'}),
			'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
		}






