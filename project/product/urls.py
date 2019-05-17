from django.conf.urls import url
from .views import product_view, SubProducts_view,manufacturer_view,productget,subproget,ProductDetail,SubProductDetail
urlpatterns = [
    url('^product/$', product_view, name='product_view'),
    url('^subproducts/$', SubProducts_view, name=' SubProducts_view'),
    url('^manufacturer/$', manufacturer_view, name = 'manufacturer_view'),
    url('^productget/$', productget, name='getall'),
    url('^subproget/$', subproget, name='subporget'),
    url(r'^get/(?P<id>[0-9A-Fa-f-]+)/$', ProductDetail.as_view()),
    url(r'^delete/(?P<id>[0-9A-Fa-f-]+)/$', ProductDetail.as_view()),
    url(r'^put/(?P<id>[0-9A-Fa-f-]+)/$', ProductDetail.as_view()),
    url(r'^getsubproduct/(?P<id>[0-9A-Fa-f-]+)/$', SubProductDetail.as_view()),
    url(r'^deletesubproduct/(?P<id>[0-9A-Fa-f-]+)/$', SubProductDetail.as_view()),
    url(r'^putsubproduct/(?P<id>[0-9A-Fa-f-]+)/$', SubProductDetail.as_view())
]