from django.contrib import admin
from models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)