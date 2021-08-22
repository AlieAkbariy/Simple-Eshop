import os

from django.db import models
from django.db.models import Q

# Create your models here.
from eshop_products_category.models import ProductCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    filename, ext = os.path.splitext(base_name)
    return filename, ext


def upload_image_path(instance, filepath):
    name, ext = get_filename_ext(filepath)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_image_path_gallery(instance, filepath):
    name, ext = get_filename_ext(filepath)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{final_name}"


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_product_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, productId):
        qs = self.get_queryset().filter(id=productId)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی')
    visit_count = models.IntegerField(default=0 , verbose_name='تعداد بازدید')

    objects = ProductManager()

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'products/{self.id}'


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_image_path_gallery, verbose_name='تصویر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name_plural = 'گالری تصاویر'
        verbose_name = 'گالری تصویر'

    def __str__(self):
        return self.title
