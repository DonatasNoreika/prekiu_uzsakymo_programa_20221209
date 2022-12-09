from django.contrib import admin
from django.urls import path, include
from .views import (OrderListView,
                    UserOrderListView,
                    UserOrderDetailView,
                    OrderCreateView,
                    OrderLineCreateView,
                    OrderUpdateView,
                    OrderDeleteView,
                    OrderLineUpdateView,
                    OrderLineDeleteView)

urlpatterns = [
    path("", OrderListView.as_view(), name="orders"),
    path("orders/", UserOrderListView.as_view(), name="user_orders"),
    path("orders/<int:pk>", UserOrderDetailView.as_view(), name="user_order"),
    path("orders/<int:pk>/newline", OrderLineCreateView.as_view(), name="order_newline"),
    path("orders/<int:pk>/edit", OrderUpdateView.as_view(), name='order_edit'),
    path("orders/<int:pk>/delete", OrderDeleteView.as_view(), name='order_delete'),
    path("order/new", OrderCreateView.as_view(), name='order_new'),
    path("orders/<int:pk2>/lineedit/<int:pk>", OrderLineUpdateView.as_view(), name='orderline_edit'),
    path("orders/<int:pk2>/linedelete/<int:pk>", OrderLineDeleteView.as_view(), name='orderline_delete'),
]