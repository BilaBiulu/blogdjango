from django.urls import reverse_lazy, reverse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post, Comment, Category
from django.shortcuts import get_object_or_404, render

class PostListView(ListView):
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)   # 404 se não existir
    posts = category.posts.order_by('-date')
    # reutiliza o template de listagem da parte 1
    return render(request, 'blog/post_list.html', {'posts': posts, 'category': category})

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