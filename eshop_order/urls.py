from django.urls import path

from eshop_order.views import add_order_user, open_order, send_request, verify, remove_order_detail

urlpatterns = [
    path('add-order-user', add_order_user),
    path('open-order', open_order),
    path('remove-order/<detail_id>', remove_order_detail),
    path('request', send_request, name='request'),
    path('verify/<order_id>', verify, name='verify'),
]
