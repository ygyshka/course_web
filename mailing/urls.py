from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import (ClientsListView, ClientsCreateView, ClientsDetailView,
                           ClientsUpdateView, ClientsDeleteView,
                           MessageListView, MessageDetailView, MessageCreateView,
                           MessageUpdateView, MessageDeleteView,
                           MailingsListView, MailingDetailView, MailingCreatView,
                           MailingUpdateView, MailingDeleteView,
                           start_page)

app_name = MailingConfig.name

urlpatterns = [
    path('', start_page, name='start_page'),
    path('clients/', ClientsListView.as_view(), name='home'),
    path('create/', ClientsCreateView.as_view(), name='create'),
    path('update/<int:pk>', ClientsUpdateView.as_view(), name='update'),
    path('client/<int:pk>', ClientsDetailView.as_view(), name='client'),
    path('delete/<int:pk>', ClientsDeleteView.as_view(), name='clients_confirm_delete'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_list/create/', MessageCreateView.as_view(), name='message_form'),
    path('message_list/update/<int:pk>', MessageUpdateView.as_view(), name='message_form'),
    path('message_list/message/<int:pk>', MessageDetailView.as_view(), name='message'),
    path('message_list/delete/<int:pk>', MessageDeleteView.as_view(), name='message_confirm_delete'),

    path('mailings_list/', MailingsListView.as_view(), name='mailing_list'),
    path('mailings_list/create/', MailingCreatView.as_view(), name='mailing_form'),
    path('mailings_list/updeate/<int:pk>', MailingUpdateView.as_view(), name='mailing_form'),
    path('message_list/mailing/<int:pk>', MailingDetailView.as_view(), name='mailing'),

]
