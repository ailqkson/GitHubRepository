from django.contrib import admin

from Fitness_blog.fitblog.models import Post, Category, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)