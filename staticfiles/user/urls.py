from django.urls import path, include

from user.views import main, login_view, profile_view, register_view

urlpatterns = [
    path('', include([
        path('auth/', login_view, name='auth'),
        path('register/', register_view, name='register'),
        path('profile', profile_view, name='profile'),
        path('logout/', login_view, name='logout'),
        path('', main, name='dashboard'),
    ]))

]
