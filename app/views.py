from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def stud(request):
    SFO=studentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        FD=studentForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
        
        
        
    return render(request,'student.html',d)
