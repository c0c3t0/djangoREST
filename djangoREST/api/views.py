from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
# from rest_framework.views import APIView

from djangoREST.api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# class ProductsListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             serializer.save()
#             return Response(status=201)
#         return Response(serializer.errors, status=400)

# class ProductsListView(ListAPIViewistAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductsListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SingleProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer