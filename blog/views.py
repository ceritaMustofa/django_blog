from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "post_detail.html"
    
class CreateNewPostView(CreateView):
    model = Post
    context_object_name = "post"
    template_name = "add_post.html"
    fields=["title", "author", "body",]
    
class UpdatePostView(UpdateView):
    model = Post
    context_object_name = "post"
    template_name = "edit_post.html"
    fields=["title", "body",]
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")