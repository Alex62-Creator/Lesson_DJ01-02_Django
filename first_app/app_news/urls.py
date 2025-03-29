from django.urls import path
from . import views

# Указываем путь к первой странице приложения app_news
urlpatterns = [
	path('', views.home, name='news_home'),
	path('create', views.create_news, name='add_news'),
]