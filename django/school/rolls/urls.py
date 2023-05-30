from django.urls import path

from . import views


app_name = 'rolls'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('searchresult/', views.searchResult, name='searchResult'),
    path('add/', views.add, name='add'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/delete/', views.dele, name='deleteit'),
    path('<int:id>/activeEdit/', views.activeEdit, name='activeEdit'),
    path('isActive/', views.active, name='active'),
    path('<int:id>/department/', views.assign, name='assign'),
    path('about/', views.about, name='about'),
]
