from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.template import loader
from django.views import View
# Create your views here.

class index(TemplateView):
    template_name = 'index.html'
