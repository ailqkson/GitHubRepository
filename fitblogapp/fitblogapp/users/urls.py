from django.urls import path

from fitblogapp.users.views import UserRegister, UserEdit

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name='edit-profile'),
    ]