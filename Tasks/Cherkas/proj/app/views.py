from django.shortcuts import render, redirect
from .models import MyModel
from .forms import AddModelPost
import datetime
from .telegram import start_message




def home(request):
    return render(request,'main.html')

def program(request):
    return render(request,'program.html')

def join_me(request):
    return render(request,'join_me.html')


     
def add_app(request):
    if request.method == 'POST':
        form = AddModelPost(request.POST, request.FILES)
        
        if form.is_valid():
            post_entry = MyModel()
            post_entry.name = form.cleaned_data['name']
            post_entry.name_of_kid = form.cleaned_data['name_of_kid']
            post_entry.class_choice = form.cleaned_data['class_choice']
            post_entry.issued = datetime.datetime.now()
            post_entry.phone = form.cleaned_data['phone']
            post_entry.comment=form.cleaned_data['comment']

            post_entry.save()
            
            start_message(f'Parent: {post_entry.name}\n Kid: {post_entry.name_of_kid}\n Number: {post_entry.phone}\n Class: {post_entry.class_choice}\n Comment: {post_entry.comment}')

            return redirect('join_me')
    else:
        form = AddModelPost()
    return render(request, 'add_app.html', {'form':form})
    