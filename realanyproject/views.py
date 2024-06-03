from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render
from realanyproject.forms import CustomUserRegistrationForm, CustomUserLoginForm, ProfileForm, SearchForm
from .models import Movie, Music, Book, CategoryModel

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
            password = form.cleaned_data['password']
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
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data.get('search_term')
            if search_term:
                music_result = Music.objects.filter(title__icontains=search_term).first()
                movie_result = Movie.objects.filter(title__icontains=search_term).first()
                book_result = Book.objects.filter(title__icontains=search_term).first()
                if music_result:
                    return redirect(f'/music/{music_result.id}')
                elif movie_result:
                    return redirect(f'/movie/{movie_result.id}')
                elif book_result:
                    return redirect(f'/book/{book_result.id}')
                else:
                    print('No results found.')
        return redirect('/')

class MusicPage(View):
    def get(self, request, pk):
        song = get_object_or_404(Music, id=pk)
        context = {'song': song}
        return render(request, 'music.html', context)

class MoviePage(View):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        context = {'movie': movie}
        return render(request, 'movie.html', context)

class BookPage(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        context = {'book': book}
        return render(request, 'book.html', context)

class CategoryPage(View):
    def get(self, request, pk):
        category = get_object_or_404(CategoryModel, id=pk)
        current_songs = Music.objects.filter(music_category=category)
        current_movies = Movie.objects.filter(movie_category=category)
        current_book = Book.objects.filter(book_category=category)
        context = {'music': current_songs, 'movie': current_movies, 'book': current_book}
        return render(request, 'category.html', context)
