from django.urls import path

from .views import ProductsList, product_detail, SearchProductView, ProductsListByCategory, product_categories_partial

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/categories/<category_name>', ProductsListByCategory.as_view()),
    path('products/search', SearchProductView.as_view()),
    path('products/<productId>', product_detail),
    path('product_categories_partial', product_categories_partial, name='product_categories_partial')
]
