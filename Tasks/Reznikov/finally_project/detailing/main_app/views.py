from django.shortcuts import render
from .forms import PopupForm
from django.http import JsonResponse, HttpRequest
from .models import Orders
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound, Http404

def index(request):
    return render(request, 'index.html')


def popup_ajax_request(request):
    if request.method == "GET":
        raise Http404

    if is_ajax(request):
        popup_form = PopupForm(request.POST)
        if popup_form.is_valid():
            popup_order = Orders()
            popup_order.date = popup_form.cleaned_data['date']
            popup_order.name = popup_form.cleaned_data['name']
            popup_order.phone = popup_form.cleaned_data['phone']
            popup_order.save()

            # popup_order.date = Orders.objects.get(date=popup_form.cleaned_data['date'])
            data = {
                'date': popup_form.cleaned_data['date'],
                'name': popup_form.cleaned_data['name'],
                'phone': popup_form.cleaned_data['phone'],
            }

            html_form = render_to_string('success.html', request=request)
            return JsonResponse({'success':data, 'html_form':html_form})
        else:
            return JsonResponse({'errors':popup_form.errors})

def popup_get_data(request):
    if request.method == "GET":
        raise Http404

    if is_ajax(request):
        popup_order = Orders()
        popup_orders = Orders.objects.filter(date__contains=request.POST['date']).values()
        
        
        convert_data = []
        for i in list(popup_orders):
            convert_data.append(i['date'])
            
        return JsonResponse({'success':convert_data})
    

def is_ajax(request: HttpRequest) -> bool:
    return (
        request.headers.get('x-requested-with') == 'XMLHttpRequest'
        or request.accepts("application/json")
    )