from django.contrib import admin
from .models import Product, Invoice,InvoiceHistory

# Register your models here.

admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(InvoiceHistory)