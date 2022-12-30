import json
from django.shortcuts import get_object_or_404, render
from foodTrackingSystem.forms import *
from django.core.exceptions import EmptyResultSet

from foodTrackingSystem.models import Product

def insert_code(request):
    if request.method == "GET":
        print('SONO NELLA GET')
        form = ProductForm()
        return render(request, 'foodTrackingSystem/insert_code.html', {'form': form})
    elif request.method == "POST":
        print('SONO NELLA POST')
        print('request.POST: ', request.POST)
        form = ProductForm(request.POST)
        # if form.is_valid(): --> PROBLEMA: FORSE AVER MESSO LA CHIAVE UNIQUE A CODE, IL FORM PER LA RICERCA VIENE FRAINTESO COME SE FOSSE PER L'INSERIMENTO NUOVO PRODOTTO
        print('form is valid')
        code = request.POST.get('code')
        print('code: ', code)
        product = Product()
        products = Product.objects.filter(code=code) # sempre singolo product
        print(products)
        if products:
            product = products.get()
            print('product: ', product)
            return render(request, 'foodTrackingSystem/product_detail.html', {'form': form, 'product': product})
        return render(request, 'foodTrackingSystem/product_detail.html', {'form': form})
        
        
        


def product_detail(request, code):
    product = get_object_or_404(Product, code=code)
    return render(request, 'foodTrackingSystem/product_detail.html')
