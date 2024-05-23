from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group, Permission


class CategoryModel(models.Model):
    category_title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'Media category'
        verbose_name_plural = 'Media categories'


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    movie = models.FileField(upload_to='Movie/Genre/movies')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    song = models.FileField(upload_to='Song/Genre/songs')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Music'
        verbose_name_plural = 'Music'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    book = models.FileField(upload_to='Book/Genre/book')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class User(AbstractUser):
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None', 'None'),
    )
    phone_number = models.CharField(max_length=13, unique=True)
    user_gender = models.CharField(max_length=7, choices=GENDERS, default='None')

    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')
    objects = UserManager()

objects = UserManager()
