from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, authenticate, login
from .models import Movie, Music, Book, CategoryModel
from realanyproject.forms import forms, CustomUserRegistrationForm, CustomUserLoginForm, SearchForm


class MovieList(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movie_list.html', {'movies': movies})

class MusicList(View):
    def get(self, request):
        music = Music.objects.all()
        return render(request, 'music_list.html', {'music': music})


class BookList(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book_list.html', {'books': books})

class HomePage(View):
    def get(self, request):
        categories = CategoryModel.objects.all()
        music = Music.objects.all()
        movie = Movie.objects.all()
        book = Book.objects.all()
        form = SearchForm()
        context = {'categories': categories, 'music': music, 'movie': movie, 'book': book, 'form': form}
        return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'signup.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password'] #Hello
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')



class Search(View):
    def post(self, request):
        if 'search_song' in request.POST:
            get_song = request.POST.get('search_song')
            try:
                exact_song = Music.objects.filter(title__icontains=get_song).first()
                if exact_song:
                    return redirect(f'/music/{exact_song.id}')
                else:
                    print('No results')
                    return redirect('/')
            except ObjectDoesNotExist:
                print('Error retrieving song')
                return redirect('/')
        elif 'search_movie' in request.POST:
            get_movie = request.POST.get('search_movie')
            try:
                exact_movie = Movie.objects.filter(title__icontains=get_movie).first()
                if exact_movie:
                    return redirect(f'/movie/{exact_movie.id}')
                else:
                    print('No results')
                    return redirect('/')
            except ObjectDoesNotExist:
                print('Error retrieving movie')
                return redirect('/')
        elif 'search_book' in request.POST:
            get_book = request.POST.get('search_book')
            try:
                exact_book = Book.objects.filter(title__icontains=get_book).first()
                if exact_book:
                    return redirect(f'/book/{exact_book.id}')
                else:
                    print('No results')
                    return redirect('/')
            except ObjectDoesNotExist:
                print('Error retrieving book')
                return redirect('/')

        return redirect('/')

class MusicPage(View):
    def get(self, request, pk):
        song = Music.objects.get(id=pk)
        context = {'song': song}
        return render(request, 'music.html', context)

class MoviePage(View):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        context = {'movie': movie}
        return render(request, 'movie.html', context)

class BookPage(View):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        context = {'book': book}
        return render(request, 'book.html', context)

class CategoryPage(View):
    def get(self, request, pk):
        category = CategoryModel.objects.get(id=pk)
        current_songs = Music.objects.filter(music_category=category)
        current_movies = Movie.objects.filter(movie_category=category)
        current_book = Book.objects.filter(book_category=category)
        context = {'music': current_songs, 'movie': current_movies, 'book': current_book}
        return render(request, 'category.html', context)

