from django.urls import path

from Fitness_blog.fitblog import views
from Fitness_blog.fitblog.views import category_view, category_list_view, article_like

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetails.as_view(), name='article-details'),
    path('article/create/', views.ArticleCreate.as_view(), name='article-create'),
    path('article/edit/<int:pk>', views.ArticleEdit.as_view(), name='article-edit'),
    path('article/delete/<int:pk>', views.ArticleDelete.as_view(), name='article-delete'),
    path('category/create', views.CategoryCreate.as_view(), name='category-create'),
    path('category/<str:cat_type>', category_view, name='category'),
    path('category_list', category_list_view, name='category-list'),
    path('like/<int:pk>', article_like, name="like-post")
]
