from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
]

# Добавляем обслуживание статических файлов в режиме разработки
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # todo
