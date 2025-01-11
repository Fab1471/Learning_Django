from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return self.name
    

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


# Loan Model
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book.title} - {self.user.username}'
