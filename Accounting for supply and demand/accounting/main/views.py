from django.shortcuts import render, redirect
from .models import Product, Invoice, InvoiceHistory
from .forms import ProductForm, InvoiceForm, InvoiceDateForm, DateForm

# Create your views here.

def main_page(request):
	return render(request, 'main/mainPage.html', {'name': 'Home',})


def product(request):
	error = ''
	products_all = Product.objects.all()

	if 'submitProd' in request.POST:
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			error = 'Form is not valid'

	if 'Edit' in request.POST:
		record_code = request.POST.get('Edit')
		return redirect(product_edit, code=record_code)

	if 'Delete' in request.POST:
		record_code = request.POST.get('Delete')
		record = Product.objects.get(code = record_code)
		record.delete()

	products = Product.objects.order_by('code')
	form = ProductForm()
	context = {
		'form': form,
		'error': error
	}

	return render(request, 'main/Products.html', {'name': 'Products', 'products': products, 'context': context})


def product_edit(request, code):
	error = ''
	record = Product.objects.get(code = code)

	if 'submitEdit' in request.POST:
		form = ProductForm(request.POST)

		if form.is_valid() or form.data['code'] == code:
			if form.data['code']:
				record.code = form.data['code']
			elif form.data['name']:
				record.name = form.data['name']
			elif form.data['category']:
				record.category = form.data['category']

			record.save()

			return redirect(product)
		else:
			error = 'Form is not valid'

	form = ProductForm()
	context = {
		'form': form,
		'error': error
	}

	return render(request, 'main/ProductsEdit.html', {'name':'Edit', 'record': record, 'context': context})


def invoice(request):
	error = ''

	if 'submit' in request.POST:
		form = InvoiceForm(request.POST)
		if form.is_valid():
			form.save()

			if Invoice.objects.all().exists():
				last_invoice = Invoice.objects.latest('name')
				invoices_history = InvoiceHistory.objects.create(name=last_invoice.name, date=last_invoice.date, sellingPrice=last_invoice.sellingPrice)
				invoices_history.save()
		else:
			error = 'Form is not valid'

	if 'Edit' in request.POST:
		record_number = request.POST.get('Edit')
		return redirect(invoice_edit, number=record_number)

	if 'Delete' in request.POST:
		record_number = request.POST.get('Delete')
		record = Invoice.objects.get(number = record_number)
		record.delete()

	invoices = Invoice.objects.order_by('number')

	form = InvoiceForm()
	context = {
		'form': form,
		'error': error
	}

	return render(request, 'main/Invoices.html', {'name': 'Invoices', 'invoices': invoices, 'context': context})


def invoice_edit(request, number):
	error = ''
	record = Invoice.objects.get(number = number)
	prev_price = record.sellingPrice

	if 'submitEdit' in request.POST:
		form = InvoiceForm(request.POST)
		if form.is_valid() or form.data['number'] == number:
			if form.data['number']:
				record.number = form.data['number']
			elif form.data['name']:
				record.name = form.data['name']
			elif form.data['customer']:
				record.customer = form.data['customer']
			elif form.data['customerName']:
				record.customerName = form.data['customerName']
			elif form.data['address']:
				record.address = form.data['address']
			elif form.data['documentSeries']:
				record.documentSeries = form.data['documentSeries']
			elif form.data['bankDetails']:
				record.bankDetails = form.data['bankDetails']
			elif form.data['sellingPrice']:
				record.sellingPrice = form.data['sellingPrice']
			elif form.data['country']:
				record.country = form.data['country']
			elif form.data['date']:
				record.date = form.cleaned_data['date']
			elif form.data['count']:
				record.count = form.data['count']
			elif form.data['factory']:
				record.factory = form.data['factory']

			record.save()

			if Invoice.objects.all().exists() and form.data['sellingPrice'] != prev_price:
				last_invoice = record
				invoices_history = InvoiceHistory.objects.create(name=last_invoice.name, date=last_invoice.date, sellingPrice=last_invoice.sellingPrice, factory=last_invoice.factory)
				invoices_history.save()

			return redirect(invoice)
		else:
			error = 'Form is not valid'

	form = InvoiceForm()
	context = {
		'form': form,
		'error': error
	}

	return render(request, 'main/InvoiceEdit.html', {'name':'Edit', 'record': record, 'context': context})


def category(request):
	records = Product.objects.values_list("category", flat=True).order_by("category").distinct()

	return render(request, 'main/Categories.html', {'name': 'Categories', 'records': records })


def customer(request):
	error = ''
	customer_date = ''
	records = []

	if request.method == 'POST':
		form = InvoiceDateForm(request.POST)
		if form.is_valid():
			customer_date = str(form.cleaned_data['date'])
		else:
			error = 'Form is not valid'

	form = InvoiceDateForm()
	context = {
		'form': form,
		'error': error
	}
	
	for element in Invoice.objects.raw(" SELECT `id`, `date`, `customerName`, `address`, MAX(`sellingPrice`) FROM `main_invoice` WHERE `date` = %s GROUP BY `customerName`", [customer_date]):
		records.append(element)

	return render(request, 'main/Customers.html', {'name': 'Customers', 'records': records, 'context': context})


def costs(request):
	error = ''
	firstDate = ''
	secondDate = ''
	records = None

	form = DateForm()
	if request.method == 'POST':
		form = DateForm(request.POST)
		if form.is_valid():
			firstDate = str(form.cleaned_data['firstDate'])
			secondDate = str(form.cleaned_data['secondDate'])

			records = InvoiceHistory.objects.filter(date__range=[firstDate,secondDate])
			print('Records', records)
		else:
			error = 'Form is not valid'

	form = DateForm()
	context = {
		'form': form,
		'error': error
	}

	return render(request, 'main/Costs.html', {'name': 'Costs', 'records': records, 'context': context})