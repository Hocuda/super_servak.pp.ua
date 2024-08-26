from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Тестовая страница
    path('test_page/', views.test_page, name='test_page'),
    # Страница для каждой темы
    path('<int:product_id>/ ', views.product, name='product'),
]
