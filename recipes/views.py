from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request,'home.html')

def sobre (request):
    return HttpResponse('Sobre')

def contato (request):
    return HttpResponse('contato')