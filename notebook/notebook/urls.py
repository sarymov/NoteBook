from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # импорт правил из приложения posts
    path('', include('my_notes.urls')),
    path('admin/', admin.site.urls),
]
