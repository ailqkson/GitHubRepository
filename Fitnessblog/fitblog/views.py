from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from Fitness_blog.fitblog.forms import PostForm, EditPostForm
from Fitness_blog.fitblog.models import Post, Category

def error_404_view(request, exeption):
    return render(request, 'base.html', {})

class HomePage(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_on']

    # query database for all categories to display in the nav bar
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

# article views

class ArticleDetails(DetailView):
    model = Post
    template_name = 'details-post.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetails, self).get_context_data(*args, **kwargs)

        likings = get_object_or_404(Post, id=self.kwargs['pk'])
        # lookup a post with id, return likes, assign them to variable
        total_likes = likings.total_likes()

        liked = False
        if likings.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["category_menu"] = category_menu
        context["total_likes"] = total_likes
        context['liked'] = liked
        return context


class ArticleCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create-post.html'


class ArticleEdit(UpdateView):
    model = Post
    form_class = EditPostForm

    template_name = 'edit-post.html'


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')


# submit a form , get back the post  with a post id,
# assign it to the post variable, then save the like to a user
def article_like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        print('unlike')
        post.likes.remove(request.user)
        liked = False
        post.save()
    else:
        print('liked')
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))


# category Views

class CategoryCreate(CreateView):
    model = Category
    template_name = 'create-category.html'
    fields = '__all__'


# query the database for categories and list all posts in that category
def category_view(request, cat_type):
    category_posts = Post.objects.filter(category=cat_type.replace('-', ' '))

    return render(request, 'categories.html',
                  ({'cat_type': cat_type.title().replace('-', ' '), 'category_posts': category_posts}))


def category_list_view(request):
    category_list = Category.objects.all()
    return render(request, 'category-list.html', {'category_list': category_list})
