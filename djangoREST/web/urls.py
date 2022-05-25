from django.urls import path

from djangoREST.web.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]


def productsAll():
    return '/api/products/'


def productDetails(id):
    return f'/api/products/{id}/'
