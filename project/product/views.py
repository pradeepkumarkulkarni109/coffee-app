    # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

import json
import jwt
from rest_framework.views import APIView

from .forms import UploadFileForm
from .models import SubProducts, Manufacturer
from rest_framework.response import Response
from .models import Products
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage
from .serializers import Productserializer,SubProductsserializer,Manfacturerserializer


@api_view(['POST','GET'])
def product_view(request):
    try:
        if request.method == 'POST':

                price = request.data.get('price')
                amount  = str(price)
                name = request.data.get('name')
                form = UploadFileForm(request.POST, request.FILES)
                if form.is_valid():
                    try:
                        # banner = request.FILES['banner']
                        main_category_img = request.FILES['main_category']
                        fs = FileSystemStorage()
                        # filename1 = fs.save(banner.name, banner)
                        filename2 = fs.save(main_category_img.name, main_category_img)
                        # uploaded_file_url1 = filename1
                        uploaded_file_url2 = filename2
                    except:
                        uploaded_file_url1 = request.data.get('banner')
                        uploaded_file_url2 = request.data.get('main_category')

                    context = {
                        # "banner": uploaded_file_url1,
                        "main_category": uploaded_file_url2,
                        "price": amount,
                        "name": name,
                    }
                    r = Products(**context)
                    r.save()
                    return Response({"message":"products added sucesfully", 'user_id':r.id, 'data':context})
                else:
                    return Response({"message":"page not found"})

    except Exception as e:
        return Response({"message": "page not found"})

##############################################################################################
@csrf_exempt
@api_view(['POST','GET'])
def SubProducts_view(request):
    try:
        if request.method == 'POST':
            old_price=request.data.get('old_price')
            new_price=request.data.get('new_price')
            weight=request.data.get('weight')
            name = request.data.get('name')
            measure=request.data.get('measure')
            tax=request.data.get('tax')
            discount=request.data.get('discount')
            description=request.data.get('description')
            form = UploadFileForm(request.POST, request.FILES)
            product_id = request.data.get('user_id')
            if form.is_valid():
                try:
                    product_image = request.FILES['product_image']
                    fs = FileSystemStorage()
                    filename3 = fs.save(product_image.name, product_image)
                    uploaded_file_url3 = filename3
                except:
                    uploaded_file_url3 = request.data.get('product_image')
            context = {
                "product_image":uploaded_file_url3,
                "old_price":old_price,
                "new_price":new_price,
                "weight": weight,
                "measure":measure,
                "tax":tax,
                "discount":discount,
                "description":description,
                "name":name,
                "product_id":product_id,
            }
            s = SubProducts(**context)
            s.save()
            return Response({"message": "products added successfully", "id":s.id, "data":context})
        else:
            return Response({"message": "page not found"})

    except Exception as e:
        return Response({"message": str(e)})

#########################################################################################################
@api_view(['POST','GET'])
def manufacturer_view(request):
    try:
        if request.method == 'POST':
            name = request.data.get('name'),
            slug=request.data.get('slug'),
            is_active=request.data.get('is_active')
            context = {
                "name": name,
                "slug": slug,
                "is_active": is_active,
            }


            m = Manufacturer(**context)
            m.save()
            return Response({"message": "manufacturer added successfully"})

        else:
            return Response({"message": "page not found"})

    except Exception as e:
        return Response({"message": "page not found"})


####################################################################################################################
@api_view(['GET'])
def productget(request):
    try:
        if request.method == 'GET':
            object = Products.objects.all()
            list=[]
            for i in object:
                context ={
                    # "banner":'/media/' + str(i.banner),
                    "main_category":'/media/' + str(i.main_category),
                    "price":i.price,
                    "name":i.name,
                }
                list.append(context)
            return Response({"contex":list})
    except Exception as e:
        return Response({"message":"request not found"})

#####################################################################################################################################
@api_view(['GET'])
def subproget(request):
    try:
        if request.method=='GET':
            object =SubProducts.objects.all()
            list=[]
            for i in object:
                context={
                    "product_id":i.product_id,
                    "product_image":'/media/'+str(i.product_image),
                    "name":i.name,
                    "old_price": i.old_price,
                    "new_price": i.new_price,
                    "weight": i.weight,
                    "description": i.description,
                    "measure": i.measure,
                    "tax": i.tax,
                    "discount": i.discount

                }
                list.append(context)
            return Response({"contex":list})
    except Exception as e:
        return Response({"message": "request not found"})



#########################################################################################################################
class ProductDetail(APIView):
   def get_object(self, id):
       try:
           return Products.objects.get(id=id)
       except Products.DoesNotExist:
           raise Http404

   def get(self, request, id):
       try:
           Products = self.get_object(id)
           serializer = Productserializer(Products)
           return Response(serializer.data)
       except Exception as e:
           return Response({'status': 'Fail', 'statuscode': '400', 'message': 'user not found'})

   def delete(self, request, id):
       try:
           users = self.get_object(id)
           users.delete()
           return Response({'status': 'success', 'statuscode': '204', 'messsage': 'usere deleted successfully'})
       except Exception as e:
           return Response({'status': 'fail', 'statuscode': '400', 'messsage': 'user not found'})

   def put(self, request, id,) :
       update = self.get_object(id)
       serializer = Products(update, data=request.data)
       try:
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
           else:
               return Response({'status': 'success', 'statuscode': '204', 'message': 'Data updatefailed'})
       except Exception as e:
           return Response({'status': 'success', 'statuscode': '204', 'message': 'invalid data'})

##################################################################################################################


class SubProductDetail(APIView):
   def get_object(self, id):
       try:
           return SubProducts.objects.get(id=id)
       except SubProducts.DoesNotExist:
           raise Http404

   def get(self, request, id):
       try:
           SubProducts = self.get_object(id)
           serializer = SubProductsserializer(SubProducts)
           return Response(serializer.data)
       except Exception as e:
           return Response({'status': 'Fail', 'statuscode': '400', 'message': 'user not found'})

   def delete(self, request, id):
       try:
           users = self.get_object(id)
           users.delete()
           return Response({'status': 'success', 'statuscode': '204', 'messsage': 'usere deleted successfully'})
       except Exception as e:
           return Response({'status': 'fail', 'statuscode': '400', 'messsage': 'user not found'})

   def put(self, request, id,) :
       update = self.get_object(id)
       serializer = SubProducts(update, data=request.data)
       try:
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
           else:
               return Response({'status': 'success', 'statuscode': '204', 'message': 'Data updatefailed'})
       except Exception as e:
           return Response({'status': 'success', 'statuscode': '204', 'message': 'invalid data'})