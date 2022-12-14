from django import forms
from .models import Post, Category

category_choices = [x for x in Category.objects.all().values_list('name', 'name')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Here'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'manahilov', 'type': 'hidden'}),
            'category': forms.Select(choices=category_choices, attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Here'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
