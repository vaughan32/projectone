from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'pk' : self.pk})