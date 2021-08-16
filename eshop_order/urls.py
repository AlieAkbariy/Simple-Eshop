from django.urls import path

from eshop_order.views import add_order_user, open_order

urlpatterns = [
    path('add-order-user', add_order_user),
    path('open-order', open_order)
]
