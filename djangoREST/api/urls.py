from django.urls import path

from djangoREST.api.views import ProductsListView

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='product list')
]