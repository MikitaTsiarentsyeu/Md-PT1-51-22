from django.shortcuts import render, redirect
from .models import Sub, Comments
from .forms import AddSubForm, AddComForm
import datetime


def home(request):

    if request.method == 'POST':
        form = AddSubForm(request.POST)
        if form.is_valid():
            sub_entry = Sub()
            sub_entry.name = form.cleaned_data['name']
            sub_entry.sub_type = form.cleaned_data['sub_type']
            sub_entry.email = form.cleaned_data['email']
            sub_entry.save()

            return render(request, 'add_sub.html', {'form': form})
    else:
        form = AddSubForm()
    return render(request, 'home.html', {'form' : form})


def add_com(request):

    if request.method == 'POST':
        form = AddComForm(request.POST)
        if form.is_valid():
            com_entry = Comments()
            com_entry.name = form.cleaned_data['name']
            com_entry.comment = form.cleaned_data['comment']
            com_entry.issued = datetime.datetime.now()
            com_entry.save()

            return redirect('comments')

    else:
        form = AddComForm()
    all_comments = Comments.objects.all()
    return render(request, 'comments.html', {'form': form, 'comments' : all_comments})
