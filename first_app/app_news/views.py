from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm

# Create your views here.
# Рендерим страницу и передаем ей список новостей
def home(request):
	# Выгружаем все новости из БД в список
	news = News_post.objects.all()
	return render(request, 'app_news/news.html', {'news': news})


def create_news(request):
	error = ''
	if request.method == 'POST':
		form = News_postForm(request.POST)  # Сюда сохранится информация от пользователя.
		if form.is_valid():
			form.save()
			return redirect('news_home')
		else:
			error = "Данные были заполнены некорректно"
	form = News_postForm()
	return render(request, 'app_news/add_news.html', {'form': form, 'error': error})