from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Product

# Create your views here.
class ProductView(APIView):

    def get(self, request: Request):
        data = []
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        if min_price and max_price:
            products = Product.objects.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            products = Product.objects.filter(price__gte=min_price)
        elif max_price:
            products = Product.objects.filter(price__lte=max_price)    
        else:
            products = Product.objects.all()
        for product in products:
            data.append({
                'id': product.id,
                'title': product.title,
                'price': product.price,
            })
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        product = Product()
        product.title = request.data.get('title')
        product.price = request.data.get('price')
        product.save()
        return Response({'message': 'Product created'}, status=status.HTTP_201_CREATED)
    
class ProductDetailView(APIView):

    def get(self, request, id):
        product = Product.objects.get(id=id)
        data = {
            'id': product.id,
            'title': product.title,
            'price': product.price,
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return Response({'message': 'Product deleted'}, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        product = Product.objects.get(id=id)
        product.title = request.data.get('title')
        product.price = request.data.get('price')
        product.save()
        return Response({'message': 'Product updated'}, status=status.HTTP_200_OK)

    

