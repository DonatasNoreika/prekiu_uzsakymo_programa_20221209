from django.contrib import admin
from django.urls import path, include
from .views import (OrderListView,
                    UserOrderListView,
                    UserOrderDetailView,
                    OrderCreateView)

urlpatterns = [
    path("", OrderListView.as_view(), name="orders"),
    path("orders/", UserOrderListView.as_view(), name="user_orders"),
    path("orders/<int:pk>", UserOrderDetailView.as_view(), name="user_order"),
    path("order/new", OrderCreateView.as_view(), name='order_new'),
]