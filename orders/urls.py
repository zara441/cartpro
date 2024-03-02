"""
URL configuration for amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from os import remove
from tabnanny import check
from django.urls import path
from . views import *


urlpatterns = [
        
        path('cart/',cart,name='cart'),
        path('add_to_cart',add_to_cart,name='add_to_cart'),
        path('remove/<order_id>',remove_item_from_cart,name="remove"),
        path('checkout',checkout,name="checkout"),
        
        path('orders',show_orders,name='orders')


    
]

