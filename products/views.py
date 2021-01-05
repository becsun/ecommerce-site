from django.views.generic import ListView
from django.shortcuts import render

from .models import Product

def product_list_view(request):
    queryset = Product.objects.all()
    template_name = "products/list.html"
    context = {
      'object_list': queryset
    }
    return render(request, "products/list.html", context)