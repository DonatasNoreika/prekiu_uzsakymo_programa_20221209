from django.shortcuts import render
from django.views import generic
from .models import Order, Product, OrderLine, Status
from django.shortcuts import reverse

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

class UserOrderDetailView(generic.DetailView):
    model = Order
    template_name = 'user_order.html'
    context_object_name = 'order'

class OrderCreateView(generic.CreateView):
    model = Order
    fields = ['status']
    success_url = "/orders"
    template_name = 'order_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OrderUpdateView(generic.UpdateView):
    model = Order
    fields = ['status', 'user']
    template_name = 'order_form.html'

    def get_success_url(self):
        return reverse('user_order', kwargs={'pk': self.kwargs['pk']})


class OrderDeleteView(generic.DeleteView):
    model = Order
    success_url = "/orders"
    template_name = 'order_delete.html'

class OrderLineCreateView(generic.CreateView):
    model = OrderLine
    fields = ['product', 'qty']
    template_name = 'orderline_form.html'

    def get_success_url(self):
        return reverse('user_order', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs['pk'])
        form.save()
        return super().form_valid(form)

class OrderLineUpdateView(generic.UpdateView):
    model = OrderLine
    fields = ['product', 'qty']
    template_name = 'orderline_form.html'

    def get_success_url(self):
        return reverse('user_order', kwargs={'pk': self.kwargs['pk2']})


class OrderLineDeleteView(generic.DeleteView):
    model = OrderLine
    template_name = 'orderline_delete.html'
    context_object_name = 'line'

    def get_success_url(self):
        return reverse('user_order', kwargs={'pk': self.kwargs['pk2']})

