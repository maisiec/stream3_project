from decimal import Decimal
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse, Http404
from paypal.standard.forms import PayPalPaymentsForm
from .models import OrderItem, Order, order_created
from .forms import OrderCreateForm
from products.models import Product
from cart.cart import Cart
from accounts.models import User


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
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
def order_list(request):
    return render(request, 'orders/list.html', {
       'orders': Order.objects.filter(user=request.user)
   })


@login_required
def order_detail(request, id):
    order = get_object_or_404(Order, user=request.user, pk=id)
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
        'currency_code': 'GBP',
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'orders/detail.html', {
        'order': order, 'form':form
    })


@login_required
def download(request, order_id, product_id):
    ''''''
    order = get_object_or_404(Order, pk=int(order_id))
    if not order.paid:
        return render(request, 'error.html')
    product = get_object_or_404(Product, pk=product_id)
    filename = product.video.name.split('/')[-1]
    response = HttpResponse(product.video, "video/mp4")
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    return response


    

       
 

    