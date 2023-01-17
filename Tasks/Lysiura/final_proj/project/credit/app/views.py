from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import  CreditRequest, Review, Consultation
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect,HttpResponseBadRequest
import datetime


    
   
    
def cred_request(request):
      if request.method == "POST":
        cred_req = CreditRequest()
        cred_req.name = request.POST.get("name")
        cred_req.surname = request.POST.get("surname")
        cred_req.patronymic = request.POST.get("lastname")
        cred_req.birthday = request.POST.get("date")
        cred_req.passport_id = request.POST.get("pass")
        cred_req.card_number = request.POST.get("card")
        cred_req.number = request.POST.get("phone")
        cred_req.sum_of_cred = request.POST.get("r1")
        cred_req.period = request.POST.get("r2")
        
        current_date = str(datetime.date.today())
        current_date = current_date.split('-')
        current_date = datetime.date(int(current_date [0]),int(current_date [1]),int(current_date [2]))
        user_date = str(cred_req.birthday)
        user_date = user_date.split('-')
        user_date = datetime.date(int(user_date[0]),int(user_date[1]),int(user_date[2]))
        diff = current_date - user_date
        diff = str(diff)
        diff = diff.split()[0]
        diff = int(diff)
        while True:
            if len(cred_req.name) > 20 or len(cred_req.name) <2:
                warning = "неверное имя!" 
                return render(request, "cred1.html", {"warning":warning})
            elif len(cred_req.surname) > 20 or len(cred_req.surname) <2:
                warning = "неверная фамилия!" 
                return render(request, "cred1.html", {"warning":warning})
            elif len(cred_req.patronymic) > 20 or len(cred_req.patronymic) <2:
                warning = "неверное отчество!" 
                return render(request, "cred1.html", {"warning":warning})
            elif len(cred_req.passport_id) != 9:
                warning = "Длина ID паспорта должна состоять из 9 символов" 
                return render(request, "cred1.html", {"warning":warning})
            elif len(cred_req.number) != 12 or not (cred_req.number).isdigit():
                warning = "Длина телефона должна состоять из 12 цифр" 
                return render(request, "cred1.html", {"warning":warning})
            elif len(cred_req.card_number) != 16 or not (cred_req.card_number).isdigit():
                warning = "неверный номер" 
                return render(request, "cred1.html", {"warning":warning})
            elif  diff < 18: 
                warning = "Вам должно быть 18 лет" 
                return render(request, "cred1.html", {"warning":warning})
            else:
                cred_req.save()
                return render(request, "cred_request.html", {"cred_req": cred_req})
      else:
        return render(request, "cred_request.html")

def consultation_request(request):
      if request.method == "POST":
        cons_req = Consultation()
        cons_req.name = request.POST.get("name")
        cons_req.email = request.POST.get("email")
        cons_req.ask = request.POST.get("your_ask")
        while True:
            if len(cons_req.name) > 20 or len(cons_req.name) < 2:
                warning = "неверное имя!" 
                return render(request, "consultation.html", {"warning":warning})
            elif len(cons_req.email) > 50 :
                warning = "неверный email!" 
                return render(request, "consultation.html", {"warning":warning})
            elif len(cons_req.ask) > 1000 :
                warning = "вопрос слишком большой!" 
                return render(request, "consultation.html", {"warning":warning})
            else:
                cons_req.save()
                return render(request, "consultation_request.html", {"cons_req": cons_req})
      else:
        return render(request, "consultation_request.html")

def review(request):
    reviews= Review.objects.all()
    return render(request, "review.html", {"reviews": reviews})

def review_quest(request):
       if request.method == "POST":
           review = Review()
           review.question = request.POST.get("question")
           review.date = datetime.datetime.now()
           while True:
                if len(review.question) > 1000:
                    warning = "слишком большой пост!" 
                    return render(request, "review.html", {"warning":warning})
                else:
                    review.save()
                    return HttpResponseRedirect("/review")

def consultation(request):
    return render(request, "consultation.html")

def detail1(request):
    return render(request, "detail1.html")

def detail2(request):
    return render(request, "detail2.html")

def detail3(request):
    return render(request, "detail3.html")

def details(request):
    return render(request, "details.html")

def cred_lizing(request):
    return render(request, "cred_lizing.html")

def cred1(request):
    return render(request, "cred1.html")

def consumer_cred(request):
    return render(request, "consumer_cred.html")
