from django.shortcuts import render, redirect
from .forms import RealtorFormCall, RealtorFormMail


def bootstrap_page_handler(request):
    error = ''
    if request.method =='POST':
        form = RealtorFormCall(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modal')
        else:
            error = 'Данные формы неверны'
            return redirect('modal_error_call')
    form = RealtorFormCall()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'index.html', context)


def advertisement(request):
    error = ''
    if request.method =='POST':
        form_mail = RealtorFormMail(request.POST)
        if form_mail.is_valid():
            form_mail.save()
            return redirect('modal')
        else:
            error = 'Данные формы неверны'
            return redirect('modal_error_mail')
    form_mail = RealtorFormMail()
    context = {
        'form_mail': form_mail,
        'error': error
    }
    return render(request, 'advertisement.html', context)

def modal(request):
    return render(request, 'modal.html')

def modal_error_call(request):
    return render(request, 'modal_error_call.html')

def modal_error_mail(request):
    return render(request, 'modal_error_mail.html')