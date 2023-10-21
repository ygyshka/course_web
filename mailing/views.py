from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Clients, Message, Mailing


# Create your views here.

class ClientsListView(ListView):
    model = Clients
    template_name = 'mailing/home.html'


class ClientsCreateView(CreateView):
    model = Clients
    form_class = ClientForm
    success_url = reverse_lazy('mailing:home')


class ClientsDetailView(DetailView):
    model = Clients
    template_name = 'mailing/client.html'


class ClientsUpdateView(UpdateView):
    model = Clients
    form_class = ClientForm
    success_url = reverse_lazy('mailing:home')


class ClientsDeleteView(DeleteView):

    model = Clients
    success_url = reverse_lazy('mailing:home')


class MessageListView(ListView):
    model = Message
    template_name = 'mailing/message_list.html'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailing/message.html'


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MailingsListView(ListView):
    model = Mailing
    success_url = reverse_lazy('mailing:message_list')


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing.html'


class MailingCreatView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(DeleteView):
    pass
