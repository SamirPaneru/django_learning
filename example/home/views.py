from django.shortcuts import redirect, render, HttpResponse
from .models import Book

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

def add_book(request):
    return render(request, 'add_book.html')

def post_book(request):
    if request.method == "POST":
        name = request.POST.get('book_name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        print(name, price, desc)
        Book.objects.create(name=name, price=price, desc=desc, author=request.user)
        return redirect('home')
    else:
        return redirect('home')