from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def resta(request, num1, num2):
    return HttpResponse('Estamos restando y el resultado es: ' + str(int(num1)-int(num2)))

def suma(request, num1, num2):
    return HttpResponse('Estamos sumando y el resultado es: ' + str(int(num1)+int(num2)))

def mult(request, num1, num2):
    return HttpResponse('Estamos multiplicando y el resultado es: ' + str(int(num1)*int(num2)))

def div(request, num1, num2):
    return HttpResponse('Estamos dividiendo y el resultado es: ' + str(int(num1)/int(num2)))

def error(request):
    return HttpResponse('No encontrado')
