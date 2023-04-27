from django.db import models
from datetime import datetime, date

# Create your models here.

class Product(models.Model):
	code = models.CharField('Code', max_length=10, unique=True, null=True, blank=True)
	name = models.CharField('Name', max_length=50, null=True, blank=True)
	category = models.CharField('Category', max_length=50, null=True, blank=True)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'


class Invoice(models.Model):
	number = models.CharField('Number', max_length=10, unique=True, null=True, blank=True)
	name = models.CharField('Name', max_length=50, null=True, blank=True)
	customer = models.CharField('Customer', max_length=20, null=True, blank=True)
	customerName = models.CharField('Customer Name', max_length=50, null=True, blank=True)
	address = models.CharField('Address', max_length=30, null=True, blank=True)
	documentSeries = models.CharField('Document Series', max_length=10, null=True, blank=True)
	bankDetails = models.CharField('Bank Details', max_length=20, null=True, blank=True)
	sellingPrice = models.IntegerField('Selling Price', null=True, blank=True)
	country = models.CharField('Country', max_length=30, null=True, blank=True)
	date = models.DateField('Date', auto_now_add=False, auto_now=False, blank=True, null=True, default='')
	count = models.CharField('Count', max_length=10, null=True, blank=True)
	factory = models.CharField('Factory Name', max_length=30, null=True, blank=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Invoice'
		verbose_name_plural = 'Invoices'


class InvoiceHistory(models.Model):
	name = models.CharField('Product Name', max_length=50)
	date = models.DateField('Date', auto_now_add=False, auto_now=False, blank=True, null=True, default='')
	sellingPrice = models.IntegerField('Selling Price')
	factory = models.CharField('Factory name', max_length=30)
	invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = 'Invoice History'
		verbose_name_plural = 'Invoices History'
