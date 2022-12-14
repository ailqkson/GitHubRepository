from django.urls import path

from fitblogapp.fitblog import views
from fitblogapp.fitblog.views import article_like, category_view, category_list_view

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('article/create', views.ArticleCreate.as_view(), name='article-create'),
    path('article/edit/<int:pk>', views.ArticleEdit.as_view(), name='article-edit'),
    path('article/delete/<int:pk>', views.ArticleDelete.as_view(), name='article-delete'),
    path('article/<int:pk>', views.ArticleDetails.as_view(), name='article-details'),
    path('category/create', views.CategoryCreate.as_view(), name='category-create'),
    path('category/<str:category>', category_view, name='category-posts'),
    path('category-list', category_list_view, name='category-list'),
    path('like/<int:pk>', article_like, name="like-post"),
    ]