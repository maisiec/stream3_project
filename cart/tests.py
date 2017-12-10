from django.test import TestCase
from forms import CartAddProductForm
from products.models import Product

# Create your tests here.

class CartTestCase(TestCase):
 # other test methods here
 def test_add_product_empty_quantity(self):
	 product_url = self.product.get_absolute_url()
	 postdata = {'product_slug': self.product.slug, 'quantity': '' }
	 response = self.client.post(product_url, postdata )
	 expected_error = unicode(CartAddProductForm.
	 base_fields['quantity'].error_messages['required'])
	 self.assertFormError(response, "form", "quantity", [expected_error])
	 
def test_add_product_zero_quantity(self):
	 product_url = self.product.get_absolute_url()
	 postdata = {'product_slug': self.product.slug, 'quantity': 0 }
	 response = self.client.post(product_url, postdata )
	 # need to concatenate the min_value onto error_text containing %s 