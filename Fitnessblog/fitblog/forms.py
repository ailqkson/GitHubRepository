from django import forms
from Fitness_blog.fitblog.models import Category
from Fitness_blog.fitblog.models import Post

# make category  choices dynamic avoid hard-coding the options for category
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for element in choices:
    choice_list.append(element)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder': 'Enter title Here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder': 'Enter title tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control-sm', 'value': '', 'id': 'Manahilov', 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control-sm', 'placeholder': 'Pick author'}),
            'category': forms.Select(choices=choice_list,
                                     attrs={'class': 'form-control-sm', 'placeholder': 'Pick category'}),
            'body': forms.Textarea(attrs={'class': 'form-control-sm', 'placeholder': 'Enter Blog text here '}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder': 'Enter title Here'}),
            # 'title_tag': forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder': 'Enter title tag'}),
            # 'author': forms.Select(attrs={'class': 'form-control-sm', 'placeholder': 'Pick author'}),
            'body': forms.Textarea(attrs={'class': 'form-control-sm', 'placeholder': 'Enter Blog text here '}),
        }
