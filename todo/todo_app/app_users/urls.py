from django.urls import path, include
from app_users.views import login_view, logout_view, AnotherLoginView, AnotherLogoutView, register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('another_login/', AnotherLoginView.as_view(), name='another_login'),
    path('another_logout/', AnotherLogoutView.as_view(), name='another_logout'),
    path('register/', register_view, name='register'),

]
