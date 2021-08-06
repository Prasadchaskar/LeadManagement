from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.models import model_to_dict
from . models import Lead


class LeadgenerationForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['client_Name','business_Type','mobile_No','email','address','requirement','department','agent_id']
    
class UpdateStatus(ModelForm):
     class Meta:
        model = Lead
        fields = ['status']