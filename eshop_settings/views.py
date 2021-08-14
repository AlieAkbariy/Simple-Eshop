from django.shortcuts import render

from eshop_settings.models import SiteSettings


# Create your views here.

def about_us_page(request):
    site_settings = SiteSettings.objects.first()
    context = {
        'site_settings': site_settings
    }
    return render(request, 'about_us/about_us_page.html', context)
