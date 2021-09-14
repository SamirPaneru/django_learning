from django import forms
from django.shortcuts import redirect, render, HttpResponse
from .models import Book
from .forms import AddBookForm
from django.contrib.auth.decorators import login_required
from auth_user.models import Author
from .models import User

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)

def detail_book_view(request, pk):
    book = Book.objects.get(pk = pk)
    context = {
        'book' : book
    }
    return render(request, 'detail_book.html', context)

def get_view(request):
    return render(request, 'get.html')

def display(request):
    if request.method == "POST":
        get_var = request.POST.get("get_name")
        return HttpResponse(f"You send {get_var} thorough POST request")
    else:
        get_var = request.GET.get("get_name")
        return HttpResponse(f"You send {get_var} thorough GET request")

@login_required
def add_book(request):
    form = AddBookForm()
    context = {'form': form}
    return render(request, 'add_book.html', context)

def post_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.cleaned_data["author"] = request.user.author
            Book.objects.create(**form.cleaned_data) # ** le dictionary ma throw gareko value harulai catch garxa
        return redirect('home')
    else:
        return redirect('home')

def profile(request, username):
    try:
        author = Author.objects.get(user=User.objects.get(username=username))
        context = {'author' : author}
    except:
        context = {'author': '404 not found'}
    return render(request, 'profile.html', context)

def 