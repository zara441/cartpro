# from email.policy import default
from django.db import models
from products.models import Product
from customers.models import Customers


# Create your models here.
class Order(models.Model):
    LIVE=1
    DELETE=0
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELEVERD=3
    ORDER_REJECTED=4
    DELETE_CHOICES=((DELETE,'Delete'),(LIVE,'Live'))
    STATUS_CHOICE=((ORDER_CONFIRMED,'ORDER_CONFIRMED'),(ORDER_PROCESSED,'ORDER_PROCESSED'),(ORDER_DELEVERD,'ORDER_DELEVERD'),(ORDER_REJECTED,'ORDER_REJECTED'))
    owner=models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)

class OrderedItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='added_carts')
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,related_name='addeditems')   
    total=models.FloatField(null=True)
    