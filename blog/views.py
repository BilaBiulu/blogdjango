from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post


class PostListView(ListView):
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')