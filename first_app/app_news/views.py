from django.shortcuts import render
from .models import News_post

# Create your views here.
# Рендерим страницу и передаем ей список новостей
def home(request):
	# Выгружаем все новости из БД в список
	news = News_post.objects.all()
	return render(request, 'app_news/news.html', {'news': news})