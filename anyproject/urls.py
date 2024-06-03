from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from realanyproject import views
from realanyproject.forms import *
from realanyproject.views import HomePage, MovieList, MusicList, BookList, Search, MusicPage, MoviePage, BookPage, CategoryPage
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('movies/', MovieList.as_view(), name='movie_list'),
    path('music/', MusicList.as_view(), name='music_list'),
    path('books/', BookList.as_view(), name='book_list'),
    # path('login/', CustomUserLoginForm.as_view(), name='login'),
    # path('logout/', CusLogout.as_view(), name='logout'),
    path('search/', Search.as_view(), name='search'),
    path('music/<int:pk>/', MusicPage.as_view(), name='music_page'),
    path('movie/<int:pk>/', MoviePage.as_view(), name='movie_page'),
    path('book/<int:pk>/', BookPage.as_view(), name='book_page'),
    path('category/<int:pk>/', CategoryPage.as_view(), name='category_page'),
    path('signup/', CustomUserRegistrationForm),
    # path('profile/', Cus, name='profile'),
]

# Статические и медиа-файлы
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
