"""media_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
from home import views
from paypal.standard.ipn import urls as paypal_urls
from payment import views as paypal_views
from products import views as product_views
from accounts.views import register, account, login, logout
from orders import views as order_views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^$', views.get_index),
    
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),

    #Account URLS
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^register/$', register, name='register'),
    url(r'^account/$', account, name='account'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    #Paypal URLS 
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^payment/', include('payment.urls', namespace='payment')),

    # Product URLS 
    url(r'^products/$', product_views.all_products, name='products'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_views.product_detail, name='product_detail'),
    url(r'^download/(?P<id>\d+)/$', order_views.download, name='download'), # view a purchase
    #url(r'^purchased/(?P<uid>\d+)/(?P<id>\d+)/$', 'products.views.purchased' ), # purchase callback
    
]

    