from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . import form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Book, BorrowedBooks
from datetime import timedelta
from django.http import HttpResponse, request
import users


# Create your views here.

def home(request):
    return render(request, 'homepage.html')


def rahma(request):
    return render(request, 'rahma.html')


def arwa(request):
    return render(request, 'arwa.html')


def yara(request):
    return render(request, 'yara.html')

def ahmed(request):
    return render(request, 'ahmed.html')


def mohammede(request):
    return render(request, 'mohammede.html')


def mohammed(request):
    return render(request, 'mohammed.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['Email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        is_staff = None
        if password1=="specialadminpass":
            is_staff = True
        else:
            is_staff =False

        if password1==password2:
            if User.objects.filter(username=username).exists():
                feedback = 'user name taken'
                print('user name taken')
                messages.info(request,'User name taken')
                return redirect('register-page')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request,'Email taken')
                return redirect('register-page')
            else:
                user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname, email=email,password = password1,is_staff=is_staff, is_superuser=is_staff)
                user.save();
                print('user created')
                return render(request,'login.html')
        else:
            print('password not matching')
            messages.info(request,'passwords not matching')
            return redirect('register-page')
    else:
       return render(request,'register.html')


def loginView(request):
    if request.method == 'POST':
       username=  request.POST.get('username')
       password =  request.POST.get('password')
       user = authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           if user.is_superuser == True:
               print('admin')
               return redirect('admin-page')
           else:
                print('student')
                return redirect('books')
    return render(request,'login.html')

def logoutView(request):
    logout(request)
    return redirect('home-page')

def profile(request):
    if request.method == 'POST':
        u_form = form.UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home-page')
    else:
        u_form = form.UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }

    return render(request, 'update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('home-page')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'updatepass.html', {
        'form': form
    })
def student(request):
    return render(request, 'books.html')


def books(request):
    search = Book.objects.all()
    searchWord = None
    if 'search-name' in request.GET:
        searchWord = request.GET['search-name']
        if searchWord:
            if search.filter(title__icontains=searchWord):
                search = search.filter(title__icontains=searchWord)
            elif search.filter(author__icontains=searchWord):
                search = search.filter(author__icontains=searchWord)
            elif search.filter(isbn__icontains=searchWord):
                search = search.filter(isbn__icontains=searchWord)
            elif search.filter(publicationYear__icontains=searchWord):
                search = search.filter(publicationYear__icontains=searchWord)

    context = {
        'books': search,
    }
    return render(request, 'books.html', context)


def adminbooks(request):
    search = Book.objects.all()
    searchWord = None
    if 'search-name' in request.GET:
        searchWord = request.GET['search-name']
        if searchWord:
            if search.filter(title__icontains=searchWord):
                search = search.filter(title__icontains=searchWord)
            elif search.filter(author__icontains=searchWord):
                search = search.filter(author__icontains=searchWord)
            elif search.filter(isbn__icontains=searchWord):
                search = search.filter(isbn__icontains=searchWord)
            elif search.filter(publicationYear__icontains=searchWord):
                search = search.filter(publicationYear__icontains=searchWord)

    context = {
        'adminBooks': search,
        'Bookform': form.AddBookForm()
    }
    return render(request, 'admin.html', context)


def booksInformation(request):
    book = Book.objects.filter(isbn=request.POST.get('show')).first()
    borrowedBook = BorrowedBooks.objects.filter(isbn=book).first()
    context = {
        'book': book,
        'borrowedBook': borrowedBook,
    }
    return render(request, 'booksInformation.html', context)


def extend(request):
    book = Book.objects.filter(isbn=request.POST.get('extend')).first()
    borrowedBook = BorrowedBooks.objects.filter(isbn=book).first()
    borrowedBook.availabilityTime = borrowedBook.borrowingDate + \
        timedelta(days=20)
    borrowedBook.isExtended = True
    borrowedBook.save()
    context = {
        'book': book,
        'borrowedBook': borrowedBook,
    }
    return render(request, 'booksInformation.html', context)


def returnBook(request):
    borrowedBook = BorrowedBooks.objects.filter(
        isbn=Book.objects.filter(isbn=request.POST.get('returnBook')).first()).first()
    borrowedBook.delete()
    return redirect('books')


def borrow(request):
    book = Book.objects.filter(isbn=request.POST.get('borrow')).first()
    borrowedBook = BorrowedBooks(isbn=book, student=request.user)
    borrowedBook.save()
    context = {
        'book': book,
        'borrowedBook': borrowedBook,
    }
    return render(request, 'booksInformation.html', context)

def adminIndex(request):  # main admin page

    if request.method == 'POST':
        add_book = form.AddBookForm(request.POST)
        if add_book.is_valid():
            add_book.save()

    context = {
        'adminBooks': Book.objects.all(),
        'Bookform': form.AddBookForm()
    }
    return render(request, 'admin.html', context)


def updateBook(request, isbn):
    book_isbn = Book.objects.get(isbn=isbn)
    if request.method == 'POST':
        book_save = form.AddBookForm(request.POST, instance=book_isbn)
        if book_save.is_valid:
            book_save.save()
            return redirect('admin-page')
    else:
        book_save = form.AddBookForm(instance=book_isbn)
    context = {
        'updateForm': book_save,
    }
    return render(request, 'updateBook.html', context)
