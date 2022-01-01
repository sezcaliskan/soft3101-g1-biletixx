import django_filters as df
from django import forms
from .models import *


class DateInput(forms.DateInput):
	input_type = 'date'

class EventFilter(df.FilterSet):
    #date = df.filters.CharFilter(label='DD-MM-YYYY')
    date = df.DateFilter(
        'date', label=('Date'),
        widget=DateInput() # I'm using a datepicker-like widget to enter date
    )

    

    class Meta:
        model = Event
        fields = ['eventtype','place','date']
        
       


