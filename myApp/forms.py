from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.models import model_to_dict
from . models import Lead


class LeadgenerationForm(ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'