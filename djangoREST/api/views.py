from django.shortcuts import render
from rest_framework import serializers, permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
# from rest_framework.views import APIView

from djangoREST.api.models import Product, Category


class IdAndNameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class IdAndNameProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')


class FullCategorySerializer(serializers.ModelSerializer):
    product_set = IdAndNameCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False)
    category = IdAndNameCategorySerializer()

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

#     access if user is authenticated:
    permission_classes = (
        permissions.IsAuthenticated,
    )


class CategoriesListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = FullCategorySerializer


class SingleProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
