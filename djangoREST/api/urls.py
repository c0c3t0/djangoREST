from django.urls import path

from djangoREST.api.views import ProductsListView, SingleProductView, CategoriesListView

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='product list'),
    path('products/<int:pk>/', SingleProductView.as_view(), name='product'),
    path('categories/', CategoriesListView.as_view(), name='category list'),
]