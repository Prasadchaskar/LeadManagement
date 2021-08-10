from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from . models import Lead
from . forms import LeadgenerationForm,UpdateStatus,UserRegisterForm
# from django.views.generic import UpdateView# Create your views here.



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
    return render(request,'myleads.html' , {'leads':leads})



def updateLead(request,id):
    obj= get_object_or_404(Lead, id=id)
        
    form = UpdateStatus(request.POST or None, instance= obj)
    context= {'form': form}

    if form.is_valid():
        obj= form.save(commit= False)

        obj.save()
        return redirect('mylead')
    else:
        context= {'form': form}
    return render(request,'updateStatus.html' , context)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})