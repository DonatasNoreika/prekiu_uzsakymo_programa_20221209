from django.contrib import admin
from django.urls import path, include
from .views import OrderListView, UserOrderListView

urlpatterns = [
    path("", OrderListView.as_view(), name="orders"),
    path("orders/", UserOrderListView.as_view(), name="user_orders"),
]