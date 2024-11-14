from django.contrib import admin
from django.urls import path
from .views.home import Index 
from .views.signup import Signup
from .views.login import Login , logout
from .views.profile import Profile1
from .middlewares.auth import  auth_middleware
from .views.search import search_customers
from .views.chat import chat_view

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('home', Index.as_view() , name='home'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    # profile
    path('profile', Profile1.as_view(), name='profile'),
    # path('users/<int:customer_id>/', Profile1.user, name='user'),
    path('logout', logout , name='logout'),
    path('search/', search_customers, name='search_customers'),

    path('requests/', Profile1.requests_page, name='requests_page'),
    path('user/<int:user_id>/', Profile1.user_profile, name='user_profile'),
    path('send-request/<int:receiver_id>/', Profile1.send_request, name='send_request'),
    path('withdraw_request/<int:request_id>/', Profile1.withdraw_request, name='withdraw_request'),
    path('accept_request/<int:request_id>/', Profile1.accept_request, name='accept_request'),
    path('reject_request/<int:request_id>/', Profile1.reject_request, name='reject_request'),
    path('notifications/', Profile1.notifications_page, name='notifications_page'),
     path('chat/<int:chat_id>/', chat_view, name='chat_view'),
]
