from django.shortcuts import render
from django.views import generic
from .models import Order, Product, OrderLine, Status

# Create your views here.
class OrderListView(generic.ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'

class UserOrderListView(generic.ListView):
    model = Order
    template_name = 'user_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


