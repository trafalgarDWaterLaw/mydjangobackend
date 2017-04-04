from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from models import users,products
from serializers import userSerializers,productSerializers



# Create your views here.


@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        userlist = users.objects.all()
        serializer = userSerializers(userlist,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = userSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        prodlist = products.objects.all()
        serializer = productSerializers(prodlist,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def product_detail(request):
    if request.method == 'GET':
        prodid = request.GET.get('prodid', None)
        prod = products.objects.get(product_id=prodid)
        serializer = productSerializers(prod,many=False)
        return Response(serializer.data)
