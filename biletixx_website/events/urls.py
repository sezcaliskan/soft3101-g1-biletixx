from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('events/list_events', views.list_events, name="list_events"),
    path('show_event/<event_id>', views.show_event, name="show_event"),
    path('add_event', views.add_event, name="add_event"),
    path('delete_event/<event_id>', views.delete_event, name="delete_event"),
    path('list_eventholder_events', views.list_eventholder_events, name="list_eventholder_events"),
    
    

    

]
