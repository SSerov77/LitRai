from django.urls import path
from django.contrib.auth import views

import users.views
from users.forms import CustomAuthenticationForm


urlpatterns = [
    path('signup/', users.views.signup, name='signup'),
    path(
        'login/', 
        views.LoginView.as_view(
            template_name='users/login.html',
            authentication_form=CustomAuthenticationForm
        ), 
        name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]


