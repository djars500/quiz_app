from django.urls import path, include
from user.views import main, login_view, profile_view, register_view, logout_view
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', include([
        path('auth/', login_view, name='auth'),
        path('register/', register_view, name='register'),
        path('profile', profile_view, name='profile'),
        path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
        path('', main, name='dashboard'),
    ]))

]
