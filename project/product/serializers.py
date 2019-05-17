from .models import Products,SubProducts,Manufacturer
from rest_framework import serializers


class Productserializer(serializers.ModelSerializer):

    photo = serializers.ImageField(max_length=None,use_url=True)


    class Meta:
        model = Products
        fields = '__all__'

class SubProductsserializer(serializers.ModelSerializer):

    photo = serializers.ImageField(max_length=None,use_url=True)


    class Meta:
        model = SubProducts
        fields = '__all__'





class Manfacturerserializer(serializers.ModelSerializer):
        model = Manufacturer
        fields = '__all__'