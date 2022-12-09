from unicodedata import name
from django.urls import path
from .views import BlogListView, PostDetailView

urlpatterns = [
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home")
]
