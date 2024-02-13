from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import View
from django import forms
from django.urls import reverse
from django.shortcuts import render

# Create your views here.

class homePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This in an app about page",
            "author": "Developed by: David",
        })
        return context
    
class ContactPageView(View):
    template_name = 'pages/contact.html'
    def get(self, request):
        viewData = {}
        viewData["email"] = "example@eafit.edu.co"
        viewData["address"] =  "cra 1231 # as - bc"
        viewData["phoneNumber"] = "3182657798"

        return render(request, self.template_name, viewData)
    
class Product:
    products = [
        {"id":"1", "name":"TV", "price": "100000", "description":"Best TV"},
        {"id":"2", "name":"iPhone", "price": "200000", "description":"Best iPhone"},
        {"id":"3", "name":"Chromecast", "price": "140000", "description":"Best Chromecast"},
        {"id":"4", "name":"Glasses", "price": "1980000", "description":"Best Glasses"}
    ]

class ProductIndexView(View):
    template_name = 'pages/products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'pages/products/show.html'


    def get(self, request, id):
        try:
            viewData = {}
            product = Product.products[int(id)-1]
            viewData["title"] = product["name"] + " - Online Store"
            viewData["subtitle"] =  product["name"] + " - Product information"
            viewData["product"] = product

            return render(request, self.template_name, viewData)
        except IndexError:
            return HttpResponseRedirect(reverse('home'))

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)
    description = forms.CharField(required=True)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price


class ProductCreateView(View):
    template_name = 'pages/products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {
            'form': form,
            'title': 'Create Product'            
        }
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']

            new_product = {
            'id': str(len(Product.products) + 1),
            'name': name,
            'price': price,
            'description': description
            }
            Product.products.append(new_product)
            return redirect('success') 
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

class SuccessPageView(TemplateView):
    template_name = 'pages/products/success.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
        })
        return context
    