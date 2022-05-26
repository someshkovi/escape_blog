from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.http import Http404
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .serializers import ProductSerializer
from .models import Product

@api_view(["GET", "POST"])
def index(request, pk=None, *args, **kwargs):
    if request.method == 'POST' and 'run_script' in request.POST:

        # import function to run
        from products.scripts import get_product_info

        # call function
        qs = Product.objects.all()
        data = ProductSerializer(qs, many=True).data
        for x in qs:
            if x.url is not None:
                response = get_product_info(x.url)
                if response:=json.loads(response):
                    price = response['price']
                    availabity_messsage = response['availabity_messsage']

        return JsonResponse(data, safe=False)

        # return user to required page
        # return HttpResponseRedirect(reverse(app_name:view_name)

    elif request.method == 'POST' and 'update_product_info_by_id' in request.POST:
        pk = int(request.POST.get('proudctId'))
        from products.scripts import get_product_info
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return HttpResponse(status=404)
        data = ProductSerializer(product).data
        if data:
            response = get_product_info(data.get('url',''))
            if response:=json.loads(response):
                price = response['price']
                availabity_messsage = response['availabity_messsage']
                data['availabity_messsage']=availabity_messsage
                data['availabity']=True
            if min_price:=data.get('min_price') is None:
                min_price = price
            min_price = min(min_price, price)
            data['min_price']=min_price
            if max_price:=data.get('max_price') is None:
                max_price = price
            max_price = max(max_price, price)
            data['max_price']=max_price
            serializer = ProductSerializer(data=response)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse(data, safe=False)


    if request.method == 'GET':
        products = Product.objects.filter(author=request.user)
        return render(request, 'products/index.html', {'products': products})


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-create/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

# @api_view(['GET'])
# def ProductList(request):
#     # print(request.user)
#     products = Product.objects.all()
#     serializers = ProductSerializer(products, many=True)
#     return Response(serializers.data)

@api_view(['GET'])
def myproductList(request):
    # print(request.user)
    products = Product.objects.all().filter(author=request.user)
    serializers = ProductSerializer(products, many=True)
    return Response(serializers.data)


class ProductList(APIView):
    """
    List all products, or create a new product.
    """
    def get(self, request, format=None):
        prouducts = Product.objects.all()
        serializer = ProductSerializer(prouducts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductDetail(APIView):
#     """
#     Retrieve, update or delete a product instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         product = self.get_object(pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


from api.permissions import IsOwnerOrReadOnly
from api.authentication import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication 
from rest_framework import permissions


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer