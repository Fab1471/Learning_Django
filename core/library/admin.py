from django.contrib import admin
from .models import Author, Category, Book, Loan

# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Loan)
