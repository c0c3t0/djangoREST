from django.urls import path

from djangoREST.api.views import ProductsListView, SingleProductView

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='product list'),
    path('products/<int:pk>', SingleProductView.as_view(), name='product'),
]