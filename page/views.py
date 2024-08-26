import time
from random import choice
from django.shortcuts import render
from .models import Stuff_card

cached_context = {}
last_time_update = 0

def refrash_index():
    global cached_context, last_time_update
    current_time = time.time()

    if current_time - last_time_update > 0.1 or current_time == None:
        objects = Stuff_card.objects.all()
        select_item = set()
        for i in range(1, 5):
            for_var = choice(objects)
            while for_var in select_item or for_var == objects.get(id=2) or for_var == objects.get(id=3):
                for_var = choice(objects)
            select_item.add(for_var)
            cached_context[f'stuff{i}'] = for_var

        last_time_update = current_time
        
    return cached_context


def index(request):
    """Главная страница"""
    context = refrash_index()
    return render(request, 'page/index.html', context)


def product(request, product_id):
    product = Stuff_card.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'page/product.html', context)


def test_page(request):
    """Страница для теста модели stuff_card"""
    stuff_card = Stuff_card.objects.all()
    context = {'stuff_card': stuff_card}
    return render(request, 'page/test_page.html', context)
