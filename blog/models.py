from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_utrl(self):
        return reverse('post_detail', kwargs={'pk': self.pk})