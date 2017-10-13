from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
	products = Products.objects.all()
	return render(request, "products/products.html", {"products":products})