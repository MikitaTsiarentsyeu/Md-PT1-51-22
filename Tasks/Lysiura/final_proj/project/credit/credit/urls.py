from django.urls import path
from app  import views
from django.contrib import admin

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("review_quest/", views.review_quest),
    path('cred_request', views.cred_request),
    path('consultation_request', views.consultation_request),
    path("consultation", views.consultation),
    path("detail1", views.detail1),
    path("detail2", views.detail2),
    path("detail3", views.detail3),
    path("details", views.details),
    path("", views.cred_lizing),
    path("cred1", views.cred1),
    path("consumer_cred", views.consumer_cred),
    path("review", views.review),
]