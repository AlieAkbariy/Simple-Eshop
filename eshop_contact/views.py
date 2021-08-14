from django.shortcuts import render

# Create your views here.
from eshop_contact.forms import ContactForm
from eshop_contact.models import ContactUs
from eshop_settings.models import SiteSettings


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    site_settings = SiteSettings.objects.first()

    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
        'site_settings':site_settings
    }
    return render(request, 'contact_us/contact_us_page.html', context)
