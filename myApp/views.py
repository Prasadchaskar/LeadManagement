from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Lead
from . forms import LeadgenerationForm
# Create your views here.

def home(request):
    return render(request,'base.html')


def leadGeneartion(request):
    if request.method == 'POST':
        form = LeadgenerationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = LeadgenerationForm()
    return render(request,'leadgenerate.html',{'form':form})


def myLeads(request):
    leads = Lead.objects.all()
    return render(request,'myleads.html',{'leads':leads})