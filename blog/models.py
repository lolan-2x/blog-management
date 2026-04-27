from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    author = models.CharField(max_length=100, default="Admin")
    category = models.CharField(max_length=50, default="General")
    excerpt = models.CharField(max_length=300, blank=True)
    tags = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"