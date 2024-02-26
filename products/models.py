from email.policy import default
from random import choices
from django.db import models

# Create your models here. creating model class for product
class Product(models.Model):
    DELETE=0
    LIVE=1
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    title=models.CharField(max_length=255)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to="images/",null=True)
    prority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    




