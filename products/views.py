from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    featured_product= Product.objects.order_by('-prority')[:4]
    latest_product= Product.objects.order_by('-id')[:4]
    context = {
        'featured_product':featured_product,
        'latest_product':latest_product
    }
    return render(request,'index.html',context)

def layout(request):
    return render(request, 'blank_layout.html')

def shop(request):
    """
    returs product list page
    we need to display product list like 4 products in row and 
    so loop over first four product in context(full product list)
    and then next using chunk function[tempaltetags(folder)-->__init__.py--->chunks.py--->function:chunk()]

    """
    page = 1
    if request.GET:
        page = request.GET.get('page',1)

    all_product= Product.objects.order_by('-prority')
    product_paginator = Paginator(all_product,3)
    product_list = product_paginator.get_page(page)
    context = {'products':product_list}
    return render(request,'shop.html',context)

def single_product(request,pk):
    """
    single product details

    """
    
    product_detail = Product.objects.get(pk=pk)
    print(product_detail)
    return render(request, 'product_details.html',{'single_product':product_detail}) 

def cart(request):
    return render(request, 'cart.html')  

