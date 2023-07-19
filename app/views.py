from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Home(TemplateView):
    template_name = 'index.html'

class Companies(TemplateView):
    template_name = 'companies.html'
    
class Login(TemplateView):
    template_name = 'login.html'
    
class Recurments(TemplateView):
    template_name = 'recurments.html'
    
class Searchjob(TemplateView):
    template_name = 'searchjob.html'
    
class Services(TemplateView):
    template_name = 'services.html'