#Импортируем класс HttpResponse
from django.http import HttpResponse

#Создаем функцию главной страницы
def index(request):
    return HttpResponse("<h1 align=center>Это мой первый проект на Django</h1>")

#Создаем функцию страницы data
def data(request):
    return HttpResponse("<h1 align=center>Это страница data</h1>")

#Создаем функцию страницы test
def test(request):
    return HttpResponse("<h1 align=center>Это страница test</h1>")
