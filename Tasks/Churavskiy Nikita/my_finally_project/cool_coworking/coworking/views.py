from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView
from .models import*
from .forms import*
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page


class BaseView(ListView):
    model = coworking
    template_name = "coworking/basebase.html"
    context_object_name = "result"
    paginate_by = 2


# def base(request):
#     result = coworking.objects.all()
#     return render(request, 'coworking/basebase.html', {'result': result} )


class AboutView(ListView):
    model = coworking
    template_name = "coworking/about.html"
    context_object_name = "result"

# def about(request):
#     result = coworking.objects.all()
#     return render(request, 'coworking/about.html', {'result': result})
    

class Adpage(LoginRequiredMixin,CreateView):
    form_class = AddPostForm
    template_name = "coworking/add_page.html"
    login_url = reverse_lazy('base')
    raise_exception = True


# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('ua_page')
#     else:
#         form = AddPostForm()

#     return render(request, 'coworking/add_page.html', {'form':form})



class ShowPost(DetailView):
    model = cities
    template_name = "coworking/show_post.html"
    context_object_name = 'city'



# def show_post(request,post_slug):
#     city = get_object_or_404(cities, slug=post_slug)
#     content = cities.objects.all()
#     context = {
#         'city': city,
#         'content': content
#     }
#     return render(request, 'coworking/show_post.html', context=context )


@login_required
def ua_page(request):
    result = Addpage.objects.all()
    city = cities.objects.all()

    content = {
    'result': result,
    'city': city,
    }

    return render(request, 'coworking/ua_page.html', content)
    

@cache_page(60*15)
def index(request):
    # result = location.objects.select_related('cat').all()
    result = location.objects.all()
    city = cities.objects.all()

    content = {
    'result': result,
    'city': city,
    }

    return render(request, 'coworking/index.html', content )


class Belarus(ListView):
    model = AboutBelarus
    template_name = "coworking/AboutBelarus.html"
    context_object_name = 'result'


class BeautifulPlaces(ListView):
    model = AboutBelarus
    template_name = "coworking/BeautifulPlaces.html"
    context_object_name = 'result'
    paginate_by = 3


class PeopleBelarus(ListView):
    model = AboutBelarus
    template_name = "coworking/PeopleBelarus.html"
    context_object_name = 'result'


class CookingBelarus(ListView):
    model = AboutBelarus
    template_name = "coworking/CookingBelarus.html"
    context_object_name = 'result'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'coworking/register.html'
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('base')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'coworking/login.html'


    def get_success_url(self):
        return reverse_lazy('base')


def Logoutuser(request):
    logout(request)
    return redirect('login')






