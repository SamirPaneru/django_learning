from django import forms
from .models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "name",
            "price",
            "desc",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "desc": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            )
        }