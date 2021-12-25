import django_filters as df
from django import forms
from .models import *



class EventFilter(df.FilterSet):
    date = df.filters.CharFilter(label='DD-MM-YYYY')

    class Meta:
        model = Event
        fields = ['eventtype','place','date']
        
       


