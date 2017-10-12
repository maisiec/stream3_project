from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.apps import AppConfig


# Create your views here.
class PaypalStoreConfig(AppConfig):
    name = 'paypal_store'


@csrf_exempt
def paypal_return(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_return.html', args)


def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_cancel.html', args)