from django.http import HttpResponse
from django.shortcuts import render
from cars.models import *


def index(request):
    posts = Cars.objects.all()
    menu = [{'title':"О сайте", 'url_name': 'about'},
            {'title': "Добавить статью", 'url_name': 'addpage'},
            {'title': "Обратная связь", 'url_name': 'contact'},
            {'title': "Авторизация", 'url_name': 'login'}
]
    context = {'posts': posts,
               'menu': menu,
               'title': Cars}
    return render(request, 'cars/index.html', context=context)

def about(request):
    return render(request, 'cars/about.html', {'menu': menu, 'title': 'О сайте'})
def show_category(request, cat_id):

    return HttpResponse(f"БУдет выводить категории{cat_id}")