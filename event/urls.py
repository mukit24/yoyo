from django.urls import path,include
from .views import event_view,event_details,add_money,create_event
urlpatterns = [
    path('',event_view,name='event_view'),
    path('<int:id>/',event_details,name='event_details'),
    path('<int:id>/add_money/',add_money,name='add_money'), 
    path('create_event/',create_event,name='create_event'),
]