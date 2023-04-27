from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('products', views.product, name='products'),
    path('products/<code>/', views.product_edit, name='productsEdit'),
    path('invoices', views.invoice, name='invoices'),
    path('invoices/<number>/', views.invoice_edit, name='invoicesEdit'),
    path('categories', views.category, name='categories'),
    path('customers', views.customer, name='customers'),
    path('costs', views.costs, name='costs'),
]