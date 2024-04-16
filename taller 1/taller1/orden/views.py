from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Orden
from django import forms

# Create your views here.

class homePageView(TemplateView):
    template_name = 'home.html'

    
    
class ver(TemplateView):
    template_name = 'ver.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Ordenes Creadas - CAOZ"
        viewData["subtitle"] =  "List of Ordenes"
        viewData["ordenes"] = Orden.objects.all()
        viewData["id"] = Orden.id 
        return render(request, self.template_name, viewData)
    
    
class mostrar(View):
    template_name = 'mostrar.html'

    def get(self, request, id):
        # Check if product id is valid
        try:
            product_id = int(id)
            if product_id < 1:
                raise ValueError("Product id must be 1 or greater")
            product = get_object_or_404(Orden, pk=product_id)
        except (ValueError, IndexError):
            # If the product id is not valid, redirect to the home page
            return redirect('home') 
        viewData = {}
        ordenes = get_object_or_404(Orden, pk=product_id)
        viewData["ID"] = ordenes.id 
        viewData["Producto1"] =  ordenes.producto1
        viewData["Producto2"] =  ordenes.producto2
        viewData["Producto3"] =  ordenes.producto3
        viewData["Producto4"] =  ordenes.producto4
        
        return render(request, self.template_name, viewData)


class ordenForm(forms.ModelForm):
    class Meta: 
        model = Orden 
        fields = ['producto1', 'producto2', 'producto3', 'producto4'] 


class crear(View):
    template_name = 'crear.html'
    
    def get(self, request):
        form = ordenForm()
        viewData = {
            'form': form,
            'title': 'Crear orden'            
        }
        return render(request, self.template_name, viewData)

    def post(self, request): 
        form = ordenForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('exito')
        else: 
            viewData = {} 
            viewData["title"] = "Crear orden" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData)
        
class exito (TemplateView):
    template_name = "exito.html"
    
class borrar(View):
    def post(self, request, id):
        order = get_object_or_404(Orden, pk=id)
        order.delete()
        return redirect('ver')