
from django.db import models
from django.contrib.auth.models import User
from customers.models import Customers
from orders.models import Order
# Create your models here.
class OrderDelivery(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    country=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.TextField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True,related_name='delivery_info')
    cart_info=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,related_name='delivery_details')
    state=models.CharField(max_length=100)
    zip=models.IntegerField()
    notes=models.TextField(null=True)