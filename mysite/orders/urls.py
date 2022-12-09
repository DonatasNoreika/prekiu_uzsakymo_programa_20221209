from django.contrib import admin
from django.urls import path, include
from .views import (OrderListView,
                    UserOrderListView,
                    UserOrderDetailView,
                    OrderCreateView,
                    OrderLineCreateView,
                    OrderUpdateView,
                    OrderDeleteView)

urlpatterns = [
    path("", OrderListView.as_view(), name="orders"),
    path("orders/", UserOrderListView.as_view(), name="user_orders"),
    path("orders/<int:pk>", UserOrderDetailView.as_view(), name="user_order"),
    path("orders/<int:pk>/newline", OrderLineCreateView.as_view(), name="order_newline"),
    path("orders/<int:pk>/edit", OrderUpdateView.as_view(), name='order_edit'),
    path("orders/<int:pk>/delete", OrderDeleteView.as_view(), name='order_delete'),
    path("order/new", OrderCreateView.as_view(), name='order_new'),
]