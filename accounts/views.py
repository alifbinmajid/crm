#from functools import total_ordering
#from multiprocessing import context
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Customer, Order, Products
from .forms import OrderForm
from .filters import OrderFilter

# Create your views here.

def home (request):
    orders = Order.objects.all()
    customer = Customer.objects.all()

    total_customer = customer.count()
    total_order = orders.count()
    delivered = orders.filter(status='deliverd').count()
    pending = orders.filter(status='pending').count()

    context = {'orders': orders,
                'customer': customer,
                'total_customer':total_customer,
                'total_order':total_order,
                'delivered':delivered,
                'pending': pending,
                }

    return render (request, 'dashboard.html', context)

def products (request):
    prod = Products.objects.all()
    return render (request, 'products.html',{'prod':prod})

def customer (request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    total_order = order.count()
    myFilter = OrderFilter(request.GET, queryset= order)
    orders = myFilter.qs
    context = {'customer': customer, 'order': order, 'total_order': total_order, 'myFilter': myFilter}
    return render (request, 'customer.html', context)

def creatOrder (request, pk):

    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form': form}
    return render (request, 'order_form.html', context)

def updateOrder (request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form': form}
    return render (request, 'order_form.html', context)

def deleteOrder (request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context ={'item': order}
    return render (request, 'delete.html', context)