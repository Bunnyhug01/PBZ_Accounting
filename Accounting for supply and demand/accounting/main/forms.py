from .models import Product, Invoice
from django.forms import ModelForm, TextInput, DateInput
from django import forms

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ["code","name","category"]
		widgets = {
			"code": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Code'
			}),
				"name": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Name'
			}),
				"category": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Category'
			}),
		}


class InvoiceForm(ModelForm):
	class Meta:
		model = Invoice
		fields = ["customer", "name", "customerName", "address", "number", "documentSeries", "bankDetails", "sellingPrice", "country", "date", "count", "factory"]
		widgets = {
				"customer": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Customer'
			}),
				"name": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Name'
			}),
				"customerName": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Customer Name'
			}),
				"address": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Address'
			}),
				"number": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Number'
			}),
				"documentSeries": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Doc. Series'
			}),
				"bankDetails": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Bank Details'
			}),
				"sellingPrice": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Price'
			}),
				"country": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Country'
			}),
				"date": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Date'
			}),
				"count": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Count'
			}),
				"factory": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Factory'
			}),
		}


class InvoiceDateForm(ModelForm):
	class Meta:
		model = Invoice
		fields = ["date"]
		widgets = {
				"date": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Date'
			}),
		}


class DateForm(forms.Form):
	firstDate = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Enter First Date', 'class': 'form-control'}))
	secondDate = forms.DateField(widget=forms.DateInput(attrs={'placeholder' :'Enter Second Date', 'class': 'form-control'}))