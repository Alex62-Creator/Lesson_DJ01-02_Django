#Импортируем класс HttpResponse и функцию render
#from django.http import HttpResponse
from django.shortcuts import render

#Создаем функцию главной страницы
def index(request):
    return render(request, 'my_app/index.html')
    #return HttpResponse("<h1 align=center>Это мой первый проект на Django</h1>")

#Создаем функцию 1 страницы
def deepseek(request):
    return render(request, 'my_app/deepseek.html')

#Создаем функцию 2 страницы
def qwen(request):
    return render(request, 'my_app/qwen.html')

#Создаем функцию 3 страницы
def hailuo(request):
    return render(request, 'my_app/hailuo.html')



# Создаем функцию страницы data
# def data(request):
#     return HttpResponse("<h1 align=center>Это страница data</h1>")
#
# Создаем функцию страницы test
# def test(request):
#     return HttpResponse("<h1 align=center>Это страница test</h1>")
