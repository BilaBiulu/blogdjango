from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post, Comment


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

class CommentCreateView(CreateView):
    model = Comment
    fields = ['author', 'text']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['pk']})