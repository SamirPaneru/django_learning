from django import forms
from django.shortcuts import redirect, render, HttpResponse
from .models import Book
from .forms import AddBookForm
from django.contrib.auth.decorators import login_required
from auth_user.models import Author
from .models import User
import os

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

@login_required
def edit_book(request, pk):
    book = Book.objects.get(pk = pk)
    if book.author.user == request.user:
        form = AddBookForm({'name': book.name, 'desc': book.desc, 'price': book.price})
        context = {'form': form}
        if request.method == 'POST':
            form = AddBookForm(request.POST)
            if form.is_valid():
                book.name, book.price, book.desc = form.cleaned_data.values()
                book.save()
                return redirect('detail_book', book.pk)
    else:
        return redirect('home')
    return render(request, 'edit_book.html', context)

@login_required
def delete_book(request, pk):
    book = Book.objects.get(pk = pk)
    if book.author.user == request.user:
        if request.method == 'POST':
            book.delete()
            return redirect('profile', request.user.username)
    else:
        return redirect('home')
    return render(request, 'delete_book.html', {'book': book})

@login_required
def profile_picture(request):
    author = Author.objects.get(user = request.user)
    if request.method == 'POST':
        picture = request.FILES.get('pic')
        # print(picture)
        author.profile_pic = picture
        author.save()
        return redirect('profile', request.user.username)
    else:
        author.profile_pic = None
    #     image_path = author.images.path
    #     #author.profile_pic.delete(save=True)
    #     #if os.path.exists(image_path):
    #     print(image_path)        
        return redirect('profile', request.user.username)

@login_required
def delete_profile_picture(request):
    author = Author.objects.get(user = request.user)
    os.remove(f'{author.profile_pic.path}')
    author.profile_pic = None
    picture = request.FILES.get('pic')
    # print(picture)
    author.profile_pic = picture
    author.save()
    print(author.profile_pic)
    return redirect('profile', request.user.username)