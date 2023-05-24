from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from cars.models import *

menu = [{'title': "История", 'url_name': 'history'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
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
    return HttpResponse('Будет возращать пункт для связи с разработчиком')


def history(request):
    return HttpResponse("Будет возвращать страницу истории создания кузова")


def login(request):
    return HttpResponse("Возращает пункт для авторизации")


def logup(request):
    return HttpResponse("Возращает пункт для регистрации")


def show_category(request, cat_id):
    return HttpResponse(f"БУдет выводить категории{cat_id}")
