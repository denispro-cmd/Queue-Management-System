from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView
from . import views
urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('register/', views.register, name='dashboard-register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='dashboard-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='dashboard-logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path('password_reset/done/',PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name = 'user/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]
