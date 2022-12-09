from unicodedata import name
from django.urls import path
from .views import BlogListView, PostDetailView, CreateNewPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path("post/add/", CreateNewPostView.as_view(), name="add_post"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<slug:slug>/edit/", UpdatePostView.as_view(), name="edit_post"),
    path("post/<slug:slug>/delete/", DeletePostView.as_view(), name="delete_post"),
    path("", BlogListView.as_view(), name="home")
]
