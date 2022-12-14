from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.urls import reverse_lazy

from fitblogapp.users.forms import SignupForm


class UserRegister(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEdit(generic.UpdateView):
    form_class = SignupForm
    template_name = 'registration/edit-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self): #????????
        return self.request.user

