from users.models import Book, BorrowedBooks
from django.contrib import admin

# Register your models here.
admin.site.register(Book),
admin.site.register(BorrowedBooks)
