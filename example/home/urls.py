from django.urls import path
from home.views import dynamci_view, index

urlpatterns = [path('', index), path('<str:string>', dynamci_view)]