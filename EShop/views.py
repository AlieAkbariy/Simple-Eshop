from django.shortcuts import render

from eshop_sliders.models import Slider


# header code behind
def header(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    context = {
        'about_us': 'این سایت توسط فریم ورک جنگو ایحاد شده است'
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
