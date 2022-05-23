from lzma import MODE_FAST
from operator import mod
from re import T
from unicodedata import name
from xml.sax import make_parser
from django.db import models

# Create your models here.

class Customer(models.Model) :
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model) :
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Products(models.Model) :
    CATAGORY=(
        ('indoor','Indoor'),
        ('outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    catagory = models.CharField(max_length=200, null=True, choices=CATAGORY)
    discription = models.CharField(max_length=400, null=True, blank=True)
    day_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model) :
    STATUS=(
        ('pending','Pending'),
        ('out of order','Out of order'),
        ('deliverd', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    dete_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name