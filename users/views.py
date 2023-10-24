from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.contrib.auth.tokens import (default_token_generator
                                        as token_generator)
from django.views.generic import UpdateView, ListView

from users.forms import MyAuthenticationForm, UserForm, ProfileUserForm
from users.models import User
from users.utils import send_email_for_verify


# Create your views here.

# login_required(login_url='users/') - декоратор для проверки прав доступа для FBV для залогиненых пользователей


class UserLoginView(LoginView):
    form_class = MyAuthenticationForm
    # form_class = UserForm
    template_name = 'users/login.html'
    success_url = 'mailing/start_page.html'


class UserLogoutView(LogoutView):
    pass


class Register(View):

    template_name = 'users/register.html'

    def get(self, request):
        context = {
            'form': UserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)
            return redirect('users:confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('mailing:start_page')

        return redirect('users:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    form_class = ProfileUserForm
    # success_url = redirect('users:profile')
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):

        return self.request.user


def generate_new_password(request):

    new_password = get_random_string(10)

    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()

    return redirect(reverse('mailing:start_page'))


class UserListView(ListView):

    model = User
    template_name = 'users/user_list.html'
    extra_context = {
        'title': 'Список пользователей'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = get_user_model().objects.all()
        return context


def activate_user(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    user.is_active = True
    user.save()
    return redirect('users:user_list')


def deactivate_user(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    user.is_active = False
    user.save()
    return redirect('users:user_list')
