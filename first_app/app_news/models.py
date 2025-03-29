from django.db import models

# Create your models here.

class News_post(models.Model):
    author = models.CharField('Автор', max_length=30)
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')

    # Выводит название новости
    def __str__(self):
        return self.title

    # Внутренний класс для перевода названия на русский
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'