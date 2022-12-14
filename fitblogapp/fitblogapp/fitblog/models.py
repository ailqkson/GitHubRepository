from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


def get_absolute_url():
    return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    POST_CATEGORY_CHOICES = [
        ('workout', 'Workout routine'),
        ('food_recipe', 'Food Recipes'),
        ('equipment', 'Equipment'),
        ('motivation', 'Motivation'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    category = models.CharField(max_length=30, default='other')
    tag_title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    date_posted = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " by " + str(self.author)

    def get_absolute_url(self):
        return reverse('article-details', args=(str(self.id)))

