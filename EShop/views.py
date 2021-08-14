from django.shortcuts import render

from eshop_sliders.models import Slider
from eshop_settings.models import SiteSettings


# header code behind
def header(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    site_settings = SiteSettings.objects.first()
    context = {
        'site_settings': site_settings
    }
    return render(request, 'shared/Footer.html', context)


# home page code behind
def home_page(request):
    sliders = Slider.objects.all()
    context = {
        'data': '',
        'sliders': sliders
    }
    return render(request, 'home_page.html', context)
