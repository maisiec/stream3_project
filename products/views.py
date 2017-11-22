from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Product
from cart.forms import CartAddProductForm




# Create your views here.

# View all products
def all_products(request):
	products = Product.objects.all()
	return render(request, "products/products.html", {"products":products})

# View each product individually
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request,
    			"products/detail.html",
    			{"product": product,
                 "cart_product_form": cart_product_form})
                   

#def download_page(request):
       ''' The page that you arrive back to from a succesful purchase'''
       #return render(request, "products/download.html", {"products":products})

#def download_link(request):
       ''' '''
      #return 