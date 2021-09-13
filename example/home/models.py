from django.db import models
from django.contrib.auth.models import User
from auth_user.models import Author

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    desc = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name