#Подключаем необходимые библиотеки и модули
from django.urls import path
from . import views

#Добавляем пути к страницам
urlpatterns = [
    path('', views.index),
    path('data', views.data),
    path('test', views.test)
]