from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField("Жанр", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Actor(models.Model):
    name = models.CharField("Имя Актера", max_length= 50)
    image = models.ImageField("Фото", upload_to="actors/")
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание", max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Film(models.Model):
    name = models.CharField("Название", max_length=100)
    image = models.ImageField("Постер", upload_to="films/")
    year = models.PositiveSmallIntegerField("Год выхода", default=0)
    country = models.CharField("Страна", max_length=70)
    description = models.TextField("Описание")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанры", related_name="film_genre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'


class Comment(models.Model):
    film = models.ForeignKey(Film, verbose_name='Чат под фидьмом', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField('Дата сообщения', default=timezone.now)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Комментырий'
        verbose_name_plural = 'Комментарии'


class Mark(models.Model):
    film = models.ForeignKey(Film, verbose_name='Оценка', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    mark = models.IntegerField(verbose_name='Оценка')
    pub_date = models.DateTimeField('Дата оценки', default=timezone.now)

    def __str__(self):
        return self.mark

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
