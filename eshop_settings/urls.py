from django.urls import path

from eshop_settings.views import about_us_page

urlpatterns = [
    path('about-us', about_us_page)
]
