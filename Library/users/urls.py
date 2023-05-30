from django import urls
from django.urls.conf import path
from users import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home-page'),
    path('books/', views.books, name='books'),
    path('adminbooks/', views.adminbooks, name='adminbooks'),
    path('register/', views.register, name='register-page'),
    path('login/', views.loginView, name='login-page'),
    path('logout/', views.logoutView, name='logout-page'),
    path('update/', views.profile, name='update-page'),
    path('about/', views.about, name='about'),
    path('about/rahma.html', views.rahma, name='rahma.html'),
    path('about/arwa.html', views.arwa, name='arwa.html'),
    path('about/yara.html', views.yara, name='yara.html'),
    path('about/ahmed.html', views.ahmed, name='ahmed.html'),
    path('about/mohammede.html', views.mohammede, name='mohammede.html'),
    path('about/mohammed.html', views.mohammed, name='mohammed.html'),
    path(r'^password/$', views.change_password, name='updatepass-page'),
    path('student/', views.student, name='student-page'),
    path('<int:isbn>', views.updateBook, name='update_book'),
    path('adminindex/', views.adminIndex, name='admin-page'),
    path('information/', views.booksInformation, name='booksInformation'),
    path('extend/', views.extend, name='extend'),
    path('return', views.returnBook, name='returnBook'),
    path('borrow/', views.borrow, name='borrow'),

]
