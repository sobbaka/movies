from django.db import models
from datetime import date

from django.urls import reverse

# Create your models here.

class Category(models.Model):
    """Категория"""
    name = models.CharField(verbose_name="Имя категории", max_length=255)
    # Подключить текстовый редактор
    description = models.TextField(verbose_name="Описание", blank=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField(verbose_name="Имя", max_length=255)
    age = models.PositiveIntegerField(verbose_name="Возраст", default=0)
    # Подключить текстовый редактор
    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"pk": self.id})

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField(verbose_name="Имя жанра", max_length=255)
    description = models.TextField(verbose_name="Описание", blank=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    tagline = models.CharField(verbose_name="Слоган", max_length=255, blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    poster = models.ImageField(verbose_name="Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField(verbose_name="Год выхода", default=2019, null=True)
    country = models.CharField(verbose_name="Страна", blank=True, max_length=100)
    directors = models.ManyToManyField(Actor, verbose_name="Режиссер", related_name="movie_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актеры", related_name="movie_actors")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    world_priemere = models.DateField("Премьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", help_text="Указывать в долларах")
    fees_world = models.PositiveIntegerField("Сборы в мире", default=0, help_text="Указывать в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    def get_review(self):
        return self.reviews.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.id})

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField(verbose_name="Описание", blank=True)
    shots = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм", related_name="shots", default=1)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр"
        verbose_name_plural = "Кадры"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фильм", related_name="rating")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        "self", verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
