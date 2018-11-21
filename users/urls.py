from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
from django.urls import include


urlpatterns = [
    path('', views.index, name='home_page'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('settings/', views.settings, name='settings'),
    path('password_reset/', auth_views.PasswordResetView.as_view()),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('list_users/', views.list_users, name='list_users')
]