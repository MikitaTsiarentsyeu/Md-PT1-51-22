from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Statement, Client, InsuranceNumber,choices_status
from .forms import  AddModelStatement, AddStatementManual
import datetime
from django.core.exceptions import ValidationError


# Create your views here
def home(request):
    return render(request, 'index.html')

def add_statement(request):
   
    if request.method == "POST":
       
        form_data = AddModelStatement(request.POST,request.FILES)

        if form_data.is_valid():

            num_form = form_data.cleaned_data['insurance_num']
            nums = InsuranceNumber.objects.filter(number=num_form).count()
            client_new = Client.objects.get(email=request.user.email) 
                      
            if nums==0:
                return render(request, 'error.html')
            elif client_new==False: 
                return render(request, 'error.html')
            else:        
                statement_entry = Statement()
                statement_entry.brand = form_data.cleaned_data['brand'] 
                statement_entry.model = form_data.cleaned_data['model'] 
                statement_entry.date_st = datetime.datetime.now()
                statement_entry.insurance_num = form_data.cleaned_data['insurance_num'] 
                statement_entry.client = Client.objects.get(email=request.user.email)
                statement_entry.status_st = choices_status[0]
    
                statement_entry.save()
                return render(request, 'complete.html')
    else:
        form = AddModelStatement()

    return render(request, 'add_form.html',{'form':form})

def error(request):
    return render(request, 'error.html')

def complete(request):
    return render(request, 'complete.html')

def statements_user(request):
    
    all_data = {}

    if request.user.is_authenticated == True:
        all_data = Statement.objects.filter(client = Client.objects.get(email=request.user.email))

    return render(request, 'statements.html', {'list_data': all_data})

def about(request):
    return render(request, 'about.html')
