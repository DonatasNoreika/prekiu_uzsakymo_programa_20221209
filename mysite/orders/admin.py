from django.contrib import admin

# Register your models here.
from .models import Product, Order, Status, OrderLine

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", 'date', 'status')
    inlines = [OrderLineInline]


admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(Status)
admin.site.register(OrderLine)