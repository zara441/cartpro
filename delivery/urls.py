from django.urls import path
from . views import *

urlpatterns = [
    path('thankyou',thankyou,name="thankyou")
]