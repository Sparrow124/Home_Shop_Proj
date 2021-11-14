from django.urls import path
from .views import *

urlpatterns = [
     path('', MainPageContent.as_view(), name='lobby_page_url'),
     path('product/<str:slug>/', ProductDetail.as_view(), name='product_detail_url'),
]
