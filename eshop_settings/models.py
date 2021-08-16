import os

from django.db import models


# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    filename, ext = os.path.splitext(base_name)
    return filename, ext


def upload_image_path(instance, filepath):
    name, ext = get_filename_ext(filepath)
    final_name = f"{instance.site_title}{ext}"
    return f"logo_image/{final_name}"


class SiteSettings(models.Model):
    site_title = models.CharField(max_length=150, verbose_name='عنوان')
    address = models.CharField(max_length=400, verbose_name='آدرس')
    phone = models.CharField(max_length=50, verbose_name='تلفن')
    mobile = models.CharField(max_length=50, verbose_name='تلفن همراه')
    fax = models.CharField(max_length=50, verbose_name='فکس')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    about_us = models.TextField(verbose_name='درباره ما', null=True, blank=True)
    copy_right = models.CharField(verbose_name='متن کپی رایت', null=True, blank=True, max_length=200)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدیریت تنظیمات'

    def __str__(self):
        return self.site_title
