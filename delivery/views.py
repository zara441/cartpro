from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from . models import  OrderDelivery
from orders.models import Order,OrderedItem
from customers.models import Customers
from products.models import Product

# Create your views here.
@login_required(login_url='customer/login')        
def thankyou(request):
    
    if request.POST:
        cart_id=request.POST['cart_id']
        
        user=request.user
        customer=user.customer_profile

        order_obj,created=Order.objects.get_or_create(owner=customer,
                                                    order_status=Order.ORDER_CONFIRMED,
                                                    id=cart_id
                                                    )
        
        if order_obj:
            order_obj.order_status=Order.ORDER_PROCESSED
            order_obj.save()
            
            # FOR COUNTING BEST SELLING PRODUCTS
            
            ordered_products=OrderedItem.objects.filter(owner=cart_id)
            pro_ids=[]
            
            for i in ordered_products:
                
                pro_ids.append(i.product.id)
            
            
            for j in pro_ids:
                product=Product.objects.get(id=j)
                
                selling_count=0
                if product:
                    selling_count += 1
                    
                    product.sold_rate += selling_count
                    product.save()
                           
        else:
            status_message="unable to process"
            messages.error(request,status_message)
            return redirect('checkout')    
        
        country=request.POST['country']
        fname=request.POST['fname']
        lname=request.POST['lname']
        address=request.POST['address']
        state=request.POST['state']
        email=request.POST['email']
        phone=request.POST['phone']
        zip=request.POST['zip']
        notes=request.POST['notes']
        
        delivery_obj=OrderDelivery.objects.create(country=country,
                                                    first_name=fname,
                                                    last_name=lname,
                                                    address=address,
                                                    email=email,
                                                phone_number=phone,state=state,zip=zip,notes=notes)
       
        
        
       
        
        
    
    
                                                 
  
    return render(request,'thankyou.html')
