from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Material, Accessory, Product, Rest
from .forms import  AddModelProduct, AddModelMaterial, AddModelAccessory
import datetime
from .templatetags import additional_functions
from django.contrib.auth.decorators import permission_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

@permission_required("handmade.add_material") #set here for add as if we can add - we can see
def materials(request):
    all_materials = Material.objects.all()
    return render(request, 'materials.html', {'materials': all_materials})

@permission_required("handmade.add_accessory")
def accessories(request):
    all_accessories = Accessory.objects.all()
    return render(request, 'accessories.html', {'accessories': all_accessories})

#allowed to see the full list of products
def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})

@permission_required("handmade.add_product")
def product(request, product_id):
    try:
        product = Product.objects.get(id = product_id)
        return render(request, 'product.html', {'product': product})
    except:
        return HttpResponseNotFound()

@permission_required("handmade.add_material")
def material(request, material_id):
    try:
        material = Material.objects.get(id = material_id)
        return render(request, 'material.html', {'material': material})
    except:
        return HttpResponseNotFound()

@permission_required("handmade.add_accessory")
def accessory(request, accessory_id):
    try:
        accessory = Accessory.objects.get(id = accessory_id)
        return render(request, 'accessory.html', {'accessory': accessory})
    except:
        return HttpResponseNotFound()

def rests(request):
    all_rests = Rest.objects.all()
    return render(request, 'rests.html', {'rests': all_rests})

@permission_required("handmade.add_product")
def add_product(request):
    if request.method == "POST":
        form = AddModelProduct(request.POST, request.FILES)
        usdrate = additional_functions.bynusd_func()
        if form.is_valid():
            product_entry = Product()
            product_entry.type = form.cleaned_data['type']
            product_entry.for_whom = form.cleaned_data['for_whom']
            product_entry.name = form.cleaned_data['name']
            product_entry.used_materials = form.cleaned_data['used_materials']
            product_entry.price_BYN = form.cleaned_data['price_BYN']
            if product_entry.price_BYN == None:
                product_entry.price_BYN = 0.0
            product_entry.price_USD = round(product_entry.price_BYN / usdrate, 3)  #form.cleaned_data['price_USD']
            product_entry.materials_price_BYN = form.cleaned_data['materials_price_BYN']
            if product_entry.materials_price_BYN == None:
                product_entry.materials_price_BYN = 0.0
            product_entry.materials_price_USD = round(product_entry.materials_price_BYN / usdrate, 3)  #form.cleaned_data['price_USD']
            product_entry.photo = form.cleaned_data['photo']
            product_entry.sell_date = form.cleaned_data['sell_date']
            if product_entry.sell_date == None:
                product_entry.sell_date = datetime.datetime.now()
            to_whom = form.cleaned_data['to_whom_was_given']
            if to_whom == None or to_whom == '':
                product_entry.to_whom_was_given = '{"Myself": "+325290000000"}'
            else:
                product_entry.to_whom_was_given = '{"' + form.cleaned_data['to_whom_was_given'].replace(":",'":"') + '"}'
            product_entry.update_timestamp = datetime.datetime.now()
            product_entry.comment = form.cleaned_data['comment']

            product_entry.save()

            return redirect("products")
        else:
            return HttpResponse('<p> Smth went wrong</p>')
    else:
        form = AddModelProduct()

    return render(request, 'add_product.html', {'form': form})

@permission_required("handmade.add_material")
def add_material(request):
    if request.method == "POST":
        form = AddModelMaterial(request.POST, request.FILES)
        usdrate = additional_functions.bynusd_func()
        if form.is_valid():
            material_entry = Material()
            material_entry.type = form.cleaned_data['type']
            material_entry.article = form.cleaned_data['article']
            material_entry.trade_mark = form.cleaned_data['trade_mark']
            material_entry.manufacturer = form.cleaned_data['manufacturer']
            if material_entry.trade_mark.lower() == 'fimo' and (material_entry.manufacturer == None or material_entry.manufacturer == ''):
                material_entry.manufacturer = 'staedtler'
            elif material_entry.trade_mark.lower() == 'cernit' and (material_entry.manufacturer == None or material_entry.manufacturer == ''):
                material_entry.manufacturer = 'the clay and paint factory'
            elif material_entry.manufacturer == None or material_entry.manufacturer == '':
                material_entry.manufacturer = 'not specified'
            material_entry.series = form.cleaned_data['series']
            material_entry.color = form.cleaned_data['color']
            material_entry.effects = form.cleaned_data['effects']
            material_entry.nominal_amount = form.cleaned_data['nominal_amount']
            if material_entry.nominal_amount == None:
                material_entry.nominal_amount = 1
            material_entry.real_amount = form.cleaned_data['real_amount']
            if material_entry.real_amount == None:
                material_entry.real_amount = material_entry.nominal_amount
            material_entry.measure_units = form.cleaned_data['measure_units']
            if material_entry.measure_units == None or material_entry.measure_units == '':
                material_entry.measure_units = 'unit'
            material_entry.unit_price_BYN = form.cleaned_data['unit_price_BYN']
            if material_entry.unit_price_BYN == None:
                material_entry.unit_price_BYN = 0.0
            material_entry.unit_price_USD = round(material_entry.unit_price_BYN / usdrate, 3)  #form.cleaned_data['price_USD']
            material_entry.purchase_date = form.cleaned_data['purchase_date']
            if material_entry.purchase_date == None:
                material_entry.purchase_date = datetime.datetime.now()
            material_entry.purchase_place = form.cleaned_data['purchase_place']
            if material_entry.purchase_place == None or material_entry.purchase_place == '':
                material_entry.purchase_place = 'found in zagashnik'
            material_entry.update_timestamp = datetime.datetime.now()
            material_entry.comment = form.cleaned_data['comment']

            material_entry.save()

            return redirect("materials")
        else:
            return HttpResponse('<p> Smth went wrong</p>')

    else:
        form = AddModelMaterial()

    return render(request, 'add_material.html', {'form': form})

@permission_required("handmade.add_material")
def add_accessory(request):
    if request.method == "POST":
        form = AddModelAccessory(request.POST, request.FILES)
        usdrate = additional_functions.bynusd_func()
        if form.is_valid():
            accessory_entry = Accessory()
            accessory_entry.type = form.cleaned_data['type']
            accessory_entry.article = form.cleaned_data['article']
            accessory_entry.manufacturer = form.cleaned_data['manufacturer']
            accessory_entry.description = form.cleaned_data['description']
            accessory_entry.unit_price_BYN = form.cleaned_data['unit_price_BYN']
            if accessory_entry.unit_price_BYN == None:
                accessory_entry.unit_price_BYN = 0.0
            accessory_entry.unit_price_USD = round(accessory_entry.unit_price_BYN / usdrate, 3)  #form.cleaned_data['price_USD']
            accessory_entry.purchase_date = form.cleaned_data['purchase_date']
            if accessory_entry.purchase_date == None:
                accessory_entry.purchase_date = datetime.datetime.now()
            accessory_entry.purchase_place = form.cleaned_data['purchase_place']
            if accessory_entry.purchase_place == None or accessory_entry.purchase_place == '':
                accessory_entry.purchase_place = 'found in zagashnik'
            accessory_entry.update_timestamp = datetime.datetime.now()
            accessory_entry.comment = form.cleaned_data['comment']

            accessory_entry.save()

            return redirect("accessories")
        else:
            return HttpResponse('<p> Smth went wrong</p>')

    else:
        form = AddModelAccessory()

    return render(request, 'add_accessory.html', {'form': form})
