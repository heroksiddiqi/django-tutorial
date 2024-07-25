from django.shortcuts import render
from django.http import HttpResponse #1


def hello(request): #2 
    return HttpResponse('hello world')
