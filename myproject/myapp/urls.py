from django.urls import path
from . import views

from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('profile/', views.ProfileView, name='profile'),
    path('adminView/', views.AdminView, name='adminView'),
	path('login/', views.user_login, name="login"),
	path('register/', views.sign_up, name='register'),
    path('logout/', views.user_logout, name='logout'),

    path('password-reset/',authViews.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/done/',authViews.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',authViews.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',authViews.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
