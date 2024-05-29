from django.shortcuts import render

def index(request):
    """Главная страница"""
    return render(request, 'page/index.html')


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
