from django.urls import include, path
from . import views

urlpatterns = [ 
    path('users/', views.UserListView.as_view(), name="auth-users-list"),
    path('register/', views.RegisterUser.as_view(), name="auth-register"),
    path('login/', views.LoginView.as_view(), name="auth-login"),
    # path('user/', views.UserAPI.as_view(), name="auth-user"),
    path('update-user/<int:pk>/', views.UpdateUserView.as_view(), name='update-user'),

    path('user/', views.UserAPI.as_view(), name="auth-user"),
    path('forgot-password/', views.ForgotPasswordAPIView.as_view(), name="forgot-password"),
    path('verify-token/<slug:token>/', views.VerifyTokenAPIView.as_view(), name="verify-token"),
    path('reset-password/', views.ResetPasswordAPIView.as_view(), name="reset-password"),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
]