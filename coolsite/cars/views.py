from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from cars.models import *

menu = [{'title': "История", 'url_name': 'history'},
        {'title': "Обратная связь", 'url_name': 'feedback'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Авторизация", 'url_name': 'login'}]


def index(request):
    posts = Cars.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница'}
    return render(request, 'cars/index.html', context=context)


def about(request):
    return render(request, 'cars/about.html', {'menu': menu, 'title': 'О сайте'})


def feedback(request):
    return render(request, 'cars/feedback.html', {'menu': menu, 'title': 'Обратная связь'})


def history(request):
    return render(request, 'cars/history.html', {'menu': menu, 'title': 'История'})


def login(request):
    return HttpResponse("Возращает пункт для авторизации")


def logup(request):
    return HttpResponse("Возращает пункт для регистрации")



def show_category(request, cat_id):
    return HttpResponse(f"БУдет выводить категории{cat_id}")
