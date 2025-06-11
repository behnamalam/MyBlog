from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ,name='index_blog'),
    path("all-posts", views.posts),
    path("all-posts/<str:slug>", views.single_post),
]
