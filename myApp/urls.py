from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('generate',views.leadGeneartion,name='generate'),
    path('mylead',views.myLeads,name='mylead')
]