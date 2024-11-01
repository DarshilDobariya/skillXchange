from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.profile import Profile1
from .middlewares.auth import  auth_middleware
from .views.search import search_customers

urlpatterns = [
    # path('', Index.as_view(), name='homepage'),
    path('', store , name='home'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    # profile
    path('profile', Profile1.as_view(), name='profile'),
    path('logout', logout , name='logout'),
    path('search/', search_customers, name='search_customers'),
]
