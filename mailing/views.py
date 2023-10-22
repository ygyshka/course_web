from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Clients, Message, Mailing, Logs


# Create your views here.

@login_required(login_url='users/')
@login_required
def start_page(request):
    client_list = Clients.objects.all()
    conntext = {
        'client_list': client_list,
        'title': 'Список клиентов'
    }
    return render(request, 'mailing/start_page.html', conntext)


class ClientsListView(LoginRequiredMixin, ListView):
    model = Clients
    template_name = 'mailing/home.html'
    extra_context = {
        'title': 'Список клиентов'
    }
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(user=self.request.user)

        return query


class ClientsCreateView(LoginRequiredMixin, CreateView):
    model = Clients
    form_class = ClientForm
    success_url = reverse_lazy('mailing:home')

    def form_valid(self, form):

        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientsDetailView(LoginRequiredMixin, DetailView):
    model = Clients
    template_name = 'mailing/client.html'


class ClientsUpdateView(LoginRequiredMixin, UpdateView):
    model = Clients
    form_class = ClientForm
    success_url = reverse_lazy('mailing:home')


class ClientsDeleteView(LoginRequiredMixin, DeleteView):

    model = Clients
    success_url = reverse_lazy('mailing:home')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'mailing/message_list.html'
    extra_context = {
        'title': 'Список сообщений'
    }

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(user=self.request.user)

        return query


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        pass


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'mailing/message.html'


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MailingsListView(LoginRequiredMixin, ListView):
    model = Mailing
    success_url = reverse_lazy('mailing:message_list')
    extra_context = {
        'title': 'Список рассылок'
    }

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(user=self.request.user)

        return query


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mailing/mailing.html'


class MailingCreatView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    pass


class LogsListView(ListView):
    model = Logs
