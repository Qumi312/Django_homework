from datetime import datetime, date, time, timedelta

from django.core.files.storage import FileSystemStorage
from django.db.models import Count, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

from .forms import ProductForm
from .models import *


# Create your views here.
@csrf_protect
def add_client(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_phone = request.POST.get('client_phone')
        client_email = request.POST.get('client_email')
        client_address = request.POST.get('client_address')
        client = Client(
            name=client_name,
            email=client_email,
            phone=client_phone,
            address=client_address,
        )
        client.save()
        return HttpResponse('OK')
    else:
        return render(request, 'add_client.html')


@csrf_protect
def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        product_quantity = request.POST.get('quantity')
        product = Product(
            name=product_name,
            description=description,
            price=price,
            quantity=product_quantity,
        )
        product.save()
        return HttpResponse('OK')
    else:
        return render(request, 'add_product.html')


@csrf_protect
def add_order(request):
    if request.method == 'POST':
        client = int(request.POST.get('client'))
        print(client)
        product = int(request.POST.get('product'))
        print(product)
        price = int(request.POST.get('price'))
        print(price)
        order = Order(
            client=client,
            product=product,
            price=price
        )
        order.save()
        return HttpResponse('OK')
    else:
        clients = Client.objects.values()
        print(clients)
        products = Product.objects.values()
        print(products)
        return render(request, 'add_order.html', {"clients": clients, 'products': products})


@csrf_protect
def products(request):
    now = timezone.now()
    if request.method == "POST":
        date_published = request.POST.get('date_published')
        if date_published == '7days':
            start_date = now - timedelta(days=7)
        elif date_published == '14days':
            start_date = now - timedelta(days=14)
        elif date_published == '30days':
            start_date = now - timedelta(days=30)
        else:
            start_date = now - timedelta(days=365)

        today_start = timezone.make_aware(datetime.combine(date.today(), time.min))
        articles = Product.objects.annotate(
            total_view_count=Count('date_published', filter=Q(date_published=start_date)),
            today_view_count=Count('date_published', filter=Q(date_published=today_start))
        ).prefetch_related('date_published').values()
        return render(request, 'products_for_date.html', {'products': articles})
    return render(request, 'products.html')

def add_image(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            fs.save(image.name, image)
            product = Product(name = name, description = description, price = price, quantity =quantity)
            product.save()
            return render(request, 'add_image.html', {'form' : form})
    else:
        form = ProductForm()
        return render(request, 'add_image.html', {'form': form})

