from django.urls import path
from home.views import index, detail_book_view

urlpatterns = [
    path('', index, name='home'),
    path('book/<int:pk>', detail_book_view, name='detail_book')
]