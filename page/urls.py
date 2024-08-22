from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница Фруктов
    path('index1/', views.index1, name='index1'),
    # Страница Овощей
    path('index2/', views.index2, name='index2'),
    # Страница Молочки
    path('index3/', views.index3, name='index3'),
    # Страница Мяса
    path('index4/', views.index4, name='index4'),
    # Тестовая страница
    path('test_page/', views.test_page, name='test_page'),
    # Страница для каждой темы
    path('<int:product_id>/', views.product, name='product'),
]
