from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditPostForm
# use generic views to do he query for us, not write it all
from fitblogapp.fitblog.models import Post, Category


# the dash replaced by space in this view, so ew can search the categories as they are in the model,
# but also not have spaces in our address bar.

def article_like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))


def category_view(request, category):
    posts = Post.objects.filter(category=category.replace('-', ' '))
    return render(request, 'categories.html',
                  {'category': category.replace('-', ' '),
                   'posts': posts})


def category_list_view(request):
    category_list = Category.objects.all()
    return render(request, 'category-list.html', {'category_list': category_list})


class HomePage(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_posted']

    # query the category model to pull out all categories,
    # and then create links for the navbar drop down mey
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


class ArticleDetails(DetailView):
    model = Post
    template_name = 'details-post.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        # to grab from our post table the primary key
        context = super(ArticleDetails, self).get_context_data(**kwargs)

        db_lookup = get_object_or_404(Post, id=self.kwargs['pk'])
        # call the function from views.py -totallikes
        total_likes = db_lookup.total_likes()

        liked = False
        if db_lookup.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["category_menu"] = category_menu
        context["total_likes"] = total_likes
        context['liked'] = liked
        return context


class ArticleCreate(CreateView):
    model = Post
    form_class = PostForm
    # fields = '__all__' - we use form class instead
    template_name = 'create-post.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleCreate, self).get_context_data(**kwargs)
        context["category_menu"] = category_menu
        return context


class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'create-category.html'


class ArticleEdit(UpdateView):
    model = Post
    form_class = EditPostForm

    template_name = 'edit-post.html'


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')
