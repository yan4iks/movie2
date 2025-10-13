from django.db import models
from django.utils import timezone
from django.urls import reverse

class Actor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя актёра")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия актёра")
    birth_date = models.DateField(verbose_name="Дата рождения")
    photo = models.ImageField(upload_to='actor_photo/', verbose_name="Фото")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Актёр"
        verbose_name_plural = "Актёры"

class Director(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя режиссёра")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия режиссёра")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"

class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name="Жанр")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    # Основная информация
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    poster = models.ImageField(upload_to='movie_posters/', verbose_name="Постер")
    release_date = models.DateField(verbose_name="Дата выхода", default=timezone.now)

    # Детали фильма
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='movies', verbose_name='Режиссёр')
    genres = models.ManyToManyField(Genre, related_name='movies', verbose_name='Жанр')
    country = models.CharField(max_length=100, verbose_name="Страна")
    duration_in_minutes = models.PositiveIntegerField(verbose_name="Продолжительность (мин)", help_text="Укажите продолжительность фильма в минутах")
    actors = models.ManyToManyField(Actor, related_name='movies', verbose_name='Актёры')

    # Финансовая информация
    budget = models.PositiveIntegerField(verbose_name="Бюджет", default=0, help_text="Укажите сумму в долларах США")
    fees_in_usa = models.PositiveIntegerField(verbose_name="Сборы в США", default=0, help_text="Укажите сумму в долларах США")
    fees_in_world = models.PositiveIntegerField(verbose_name="Сборы в мире", default=0, help_text="Укажите сумму в долларах")

    # Рейтинг и служебная информация
    reting_imb = models.FloatField(verbose_name="Рейтинг Кинопоиск", default=0.0)
    is_published = models.BooleanField(verbose_name="Опубликовано", default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


