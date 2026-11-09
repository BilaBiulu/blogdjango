from django import forms
from. models import Post

class PostFrom(forms.ModelFrom):
    class Meta:
        model = Post
        fields = ['title', 'content']