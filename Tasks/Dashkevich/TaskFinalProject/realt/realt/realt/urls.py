from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bootstrap_page_handler, name='home'),
    path('advertisement', views.advertisement, name='advertisement'),
    path('modal', views.modal, name='modal'),
    path('modal_error_call', views.modal_error_call, name='modal_error_call'),
    path('modal_error_mail', views.modal_error_mail, name='modal_error_mail'),
]
