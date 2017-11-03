from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Product


# Create your views here.

# View all products
def all_products(request):
	products = Product.objects.all()
	return render(request, "products/products.html", {"products":products})

# View each product individually
def product_detail(request, id):
	product_detail = get_object_or_404(Product, pk=id)
	return render(request, "products/product_details.html",{"product_detail":product_detail})

def download_page(request):
	''' The page that you arrive back to from a succesful purchase'''
	return render(request, "products/download.html", {"products":products})

def download_link(request):
	''' '''
	return 


