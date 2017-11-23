from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^create/$', views.order_create, name='order_create'),
	url(r'^(?P<id>\d+)/$', views.order_detail, name='detail'),
	url(r'^$', views.order_list, name='list'),
]