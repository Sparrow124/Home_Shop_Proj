from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import View
from .utils import *


class MainPageContent(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products/main_page.html', context={'products': products})


class ProductDetail(ObjectDetailMixin, View):
    model = Product
    template = 'products/prod_info.html'
