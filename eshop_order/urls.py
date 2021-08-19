from django.urls import path

from eshop_order.views import add_order_user, open_order, send_request, verify

urlpatterns = [
    path('add-order-user', add_order_user),
    path('open-order', open_order),
    path('request', send_request, name='request'),
    path('verify', verify, name='verify'),
]
