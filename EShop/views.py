import itertools

from django.shortcuts import render

from eshop_products.models import Product
from eshop_settings.models import SiteSettings
from eshop_sliders.models import Slider


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))





# header code behind
def header(request, *args, **kwargs):
    site_settings = SiteSettings.objects.first()
    context = {
        'site_settings': site_settings
    }
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
    most_visited_product = Product.objects.order_by('visit_count').all()[:8]
    latest_product = Product.objects.order_by('id').all()[:8]
    context = {
        'data': '',
        'sliders': sliders,
        'most_visited_product': my_grouper(4, most_visited_product),
        'latest_product': my_grouper(4, latest_product)
    }
    return render(request, 'home_page.html', context)
