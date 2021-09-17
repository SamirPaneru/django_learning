from django.urls import path
from home.views import edit_book, get_view, index, detail_book_view, display, add_book, post_book, profile, delete_book, profile_picture

urlpatterns = [
    path('', index, name='home'),
    path('book/<int:pk>', detail_book_view, name='detail_book'), # yo name chai href url ma use hunxa
    path('get_view', get_view, name='get_view'),
    path('display', display, name='display'),
    path('add_book', add_book, name='add_book'),
    path('post_book', post_book, name='post_book'),
    path('user/<str:username>', profile, name='profile'),
    path('edit_book/<int:pk>', edit_book, name='edit_book'),
    path('delete_book/<int:pk>', delete_book, name='delete_book'),
    path('profile_picture', profile_picture, name='profile_picture'),
]