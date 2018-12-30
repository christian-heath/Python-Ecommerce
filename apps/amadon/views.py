from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Product

def index(request):
    context = {
        'products': Product.objects.all().values()
    }
    return render(request, 'amadon/index.html', context)
    
def buy(request):
    if request.method == 'POST':
        order = Product.objects.get(id=request.POST['id'])
        request.session['price'] = order.price * int(request.POST['quantity'])
        if 'total_spent' not in request.session:
            request.session['total_spent'] = 0
        request.session['total_spent'] += request.session['price']
        if 'num_products' not in request.session:
            request.session['num_products'] = 0
        request.session['num_products'] +=int(request.POST['quantity'])
        return redirect('/checkout')
    else:
        return redirect('/')

def checkout(request):
    return render(request, 'amadon/checkout.html')