from django.urls import path, include

from .views import products_view, product_details_view, category_list

app_name = 'shop'

urlpatterns = [
    path('', products_view, name='products'),
    path('<slug:slug>/', product_details_view, name='product-detail'),
    path('search/<slug:slug>/', category_list, name='category-list'),
]
