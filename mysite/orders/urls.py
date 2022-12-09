from django.contrib import admin
from django.urls import path, include
from .views import OrderListView

urlpatterns = [
    path("", OrderListView.as_view(), name="orders"),
]