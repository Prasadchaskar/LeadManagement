from django.urls import path
from . import views

urlpatterns = [
    path('generate',views.leadGeneartion,name='generate'),
    path('',views.myLeads,name='mylead'),
    path('update/<int:id>/',views.updateLead,name='update'),
 
]