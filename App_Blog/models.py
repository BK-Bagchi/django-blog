from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(
        User, related_name='post_author', on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=264, verbose_name='Put a title')
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name='What is on your mind?')
    blog_image = models.ImageField(
        upload_to='blog_images', verbose_name='Image')
    published_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date', ]

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date', ]

    def __str__(self):
        return self.comment


class Likes(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='liked_blog')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='liked_user')

    def __str__(self):
        return f'{self.user} likes {self.blog}'
