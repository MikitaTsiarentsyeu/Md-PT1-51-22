from django.contrib import admin
from django.urls import path, include
from .views import*
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(BaseView.as_view()), name = 'base'),
    path('about/', AboutView.as_view() , name = 'about'),
    path('add_page/', Adpage.as_view() , name = 'add_page'),
    path('coworkingbelarus/<slug:slug>/', cache_page(60)(ShowPost.as_view()) , name = 'post'),
    path('Aboutbelarus/', Belarus.as_view() , name = 'AboutBelarus'),
    path('BeautifulPlaces/', cache_page(60)(BeautifulPlaces.as_view()) , name = 'BeautifulPlaces'),
    path('PeopleBelarus/', PeopleBelarus.as_view() , name = 'PeopleBelarus'),
    path('CookingBelarus/', CookingBelarus.as_view() , name = 'CookingBelarus'),
    path('register/', RegisterUser.as_view() , name = 'register'),
    path('login/', LoginUser.as_view() , name = 'login'),
    path('logout/', Logoutuser , name = 'logout'),
    path('coworkingbelarus/', index , name = 'index'),
    path('ua_page/', ua_page , name = 'ua_page'),
    
]
