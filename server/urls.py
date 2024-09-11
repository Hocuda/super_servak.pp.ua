from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('servachok/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('page.urls')),
]

# Добавляем обслуживание статических файлов в режиме разработки
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)