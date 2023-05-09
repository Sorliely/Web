from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("xnjdklsjf")

def show_category(request, cat_id):

    return HttpResponse(f"БУдет выводить категории{cat_id}")