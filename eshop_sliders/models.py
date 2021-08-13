import os

from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    filename, ext = os.path.splitext(base_name)
    return filename, ext


def upload_image_path(instance, filepath):
    name, ext = get_filename_ext(filepath)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"sliders/{final_name}"


# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    link = models.URLField(max_length=100, verbose_name='ادرس')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title
