from django.urls import path
from home.views import get_view, index, detail_book_view, display

urlpatterns = [
    path('', index, name='home'),
    path('book/<int:pk>', detail_book_view, name='detail_book'), # yo name chai href url ma use hunxa
    path('get_view', get_view, name='get_view'),
    path('display', display, name='display'),
]