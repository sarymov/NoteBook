from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком мороженого
    path('my_notes/', views.my_notes_list),
    # Страница с информацией об одном сорте мороженого;
    # в качестве параметра ожидает целое положительное число или 0
    path('my_notes/<int:pk>/', views.my_notes_detail),
    path('group_notes/<slug:pk>/', views.group_notes),
]
