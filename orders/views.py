from django.shortcuts import render, redirect, get_list_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import OrderItem, Order, order_created
from .forms import OrderCreateForm
from cart.cart import Cart
from accounts.models import User


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],)
            # clear the cart
            cart.clear()
            # send confirmation email
            order_created(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect to the payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})

@login_required
def download(request, id):
    ''''''
    product = get_object_or_404(models.Product, pk=id)
    try:
        #purchased = models.Purchase.objects.get( product=product, purchaser=request.user)
        f = open( settings.RESOURCES_DIR, "r")
        data = f.read()
        f.close ()
        # return items as file
        response = HttpResponse(data)
        response['Content-Disposition'] = 'attachment; filename=%s' 
        return response
    except models.Purchase.DoesNotExist: 
        return render_to_response("cart/detail.html", {"products":products})

    