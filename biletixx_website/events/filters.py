import django_filters

from .models import *



class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['place', 'eventtype', 'date', ]