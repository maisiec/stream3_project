import uuid
from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField
from paypal.standard.forms import PayPalPaymentsForm
from django.core.urlresolvers import reverse

# Create your models here.
# class ProductTag(models.Model):
#     '''
    
#     '''
#     name = models.CharField()
#     slug = models.SlugField(unique=True)

# class ProductTagItem(models.Model):
#     tag = models.ForeignKey(ProductTag)
#     product = models.ForeignKey("Product")


class Product(models.Model):

    '''
    Product.objects.filter(producttagitem__set__tag='paris')
    '''
    name = models.CharField(max_length=254, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    video = models.FileField(upload_to='product_videos')


    class Meta:
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency_code": "GBP",
            "item_name": self.name,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }
 
        return PayPalPaymentsForm(initial=paypal_dict)
 
    def __unicode__(self):
        return self.name




