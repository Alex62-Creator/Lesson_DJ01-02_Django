#Подключаем необходимые библиотеки и модули
from django.urls import path
from . import views

#Добавляем пути к страницам
urlpatterns = [
    path('', views.index, name='home'),
    path('deepseek', views.deepseek, name='page1'),
    path('qwen', views.qwen, name='page2'),
    path('hailuo', views.hailuo, name='page3'),
    #path('data', views.data),
    #path('test', views.test)
]