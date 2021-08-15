from django.urls import path

from eshop_order.views import add_order_user

urlpatterns = [
    path('add-order-user', add_order_user)
]
