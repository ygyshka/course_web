from django.urls import path
from django.views.generic import TemplateView

from users.apps import UserConfig
from users.views import (UserLogoutView, Register, EmailVerify,
                         ProfileUpdateView, generate_new_password, UserLoginView,
                         UserListView,
                         deactivate_user, activate_user)

app_name = UserConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user_view', UserListView.as_view(), name='user_list'),
    path('register/', Register.as_view(), name='register'),
    path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'), name='confirm_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'), name='invalid_verify'),
    path(
        'veryfi_email/<uidb64>/<token>/',
        EmailVerify.as_view(),
        name='verify_email',
    ),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/genpass', generate_new_password, name='generate_new_password'),

    path('deactivate_user/<int:pk>', deactivate_user, name='deactivate_user'),
    path('activate_user/<int:pk>', activate_user, name='activate_user'),

]
