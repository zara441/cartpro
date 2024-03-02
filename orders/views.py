from venv import create
from django.shortcuts import redirect, render
from . models import Order,OrderedItem
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

 

# Create your views here.

@login_required(login_url='customer/login')
def show_orders(request):
    user=request.user
    customer=user.customer_profile
    all_orders_of_customer=Order.objects.filter(owner_id=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders_of_customer}
    return render(request,'orders.html',context)



@login_required(login_url='customer/login')
def cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
        )
    context={'cart':cart_obj}
    return render(request, 'cart.html',context) 


def add_to_cart(request):
    
    if request.POST:
        user_details= request.user
        
        customer=user_details.customer_profile
        
        quantity=int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        product=Product.objects.get(pk=product_id)
         
        # we are creating cart object (adding values to Order table)

        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        
        # creating orderitem

        order_items,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj
        )
        if created:
            order_items.quantity=quantity
            order_items.save()
        else:
            order_items.quantity += quantity   
            order_items.save() 
        # order_items.product.price=order_items.product.price * order_items.quantity
        # total=order_items.product.price
        
        return redirect('cart')
    

def remove_item_from_cart(request,order_id):
    instance_id=OrderedItem.objects.get(id=order_id)
    if  instance_id:
        instance_id.delete()
    return redirect('cart')

@login_required(login_url='customer/login')
def checkout(request):
    products=[]
    
    if request.POST:
        
        cart_id=int(request.POST['cart_id'])
        cart=Order.objects.get(id=cart_id)
        orderitems=OrderedItem.objects.filter(owner_id=cart_id)
        if orderitems:

            for items in orderitems:
                
                if cart_id==items.owner_id:
                    products.append(items)

            context={'items':products,'cart':cart,'cart_id':cart_id}
            
            user=request.user
            customer=user.customer_profile
            order_obj,created=Order.objects.get_or_create(owner=customer,
                                                    order_status=Order.CART_STAGE
                                                    )
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.save()
            
        else:
            status_message="unable to process,No items in the cart"
            messages.error(request,status_message)
            return redirect('cart')
    return render(request,'checkout.html',context)   
 
