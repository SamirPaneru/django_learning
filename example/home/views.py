from django.shortcuts import render, HttpResponse
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dynamci_view(request, string):
    return HttpResponse(string)