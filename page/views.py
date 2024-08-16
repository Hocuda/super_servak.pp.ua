import time
from random import choice
from django.shortcuts import render
from .models import Stuff_card

cached_context = None
last_time_update = 0

def refrash_index():
    global cached_context, last_time_update
    current_time = time.time()

    if current_time - last_time_update > 60 or current_time == None:
        objects = Stuff_card.objects.all()
        cached_context = {'stuff1': choice(objects),
                    'stuff2': choice(objects),
                    'stuff3': choice(objects),
                    'stuff4': choice(objects),}
        last_time_update = current_time
        
    return cached_context

def index(request):
    """Главная страница"""
    context = refrash_index()
    return render(request, 'page/index.html', context)


def index1(request):
    """Страница 'мясо'"""
    return render(request, 'page/index1.html')


def index2(request):
    """Страница 'овощи'"""
    return render(request, 'page/index2.html')


def index3(request):
    """Страница 'фрукты'"""
    return render(request, 'page/index3.html')


def index4(request):
    """Страница 'напитки'"""
    return render(request, 'page/index4.html')


def test_page(request):
    """Страница для теста модели stuff_card"""
    stuff_card = Stuff_card.objects.all()
    context = {'stuff_card': stuff_card}
    return render(request, 'page/test_page.html', context)
