from django.urls import path
from . import views
from .views import SignupView, LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
