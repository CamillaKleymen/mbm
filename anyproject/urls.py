"""
URL configuration for anyproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from realanyproject import views
from realanyproject.forms import register, profile
from realanyproject.views import HomePage, MovieList, MusicList, BookList, Search, MusicPage, MoviePage, BookPage, CategoryPage
from user.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from realanyproject.views import home_page, MyLoginView, logout_view, search, music_page,  category_page

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('movies/', views.MovieList.as_view(), name='movie_list'),
    path('music/', views.MusicList.as_view(), name='music_list'),
    path('books/', views.BookList.as_view(), name='book_list'),
    path('login/', views.MyLogin.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('search/', Search.as_view(), name='search'),
    path('music/<int:pk>/', MusicPage.as_view(), name='music_page'),
    path('movie/<int:pk>/', views.MoviePage.as_view(), name='movie_page'),
    path('book/<int:pk>/', views.BookPage.as_view(), name='book_page'),
    path('category/<int:pk>/', views.CategoryPage.as_view(), name='category_page'),
    path('admin/', admin.site.urls),
    path('signup/', register),
    path('profile/', profile, name='profile'),
]



urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
