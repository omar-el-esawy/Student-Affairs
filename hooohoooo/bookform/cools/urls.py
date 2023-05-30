from django.urls import path

from . import views


urlpatterns = [
    path('', views.indexView),
    path('post/ajax/friend', views.postFriend, name="post_friend"),
    path('get/ajax/validate/nickname',
         views.checkNickName, name="validate_nickname")


]
