from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(black=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_utrl(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCAD, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.author} em {self.post}'