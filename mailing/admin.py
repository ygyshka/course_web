from django.contrib import admin

from mailing.models import Clients, Message, Mailing


# Register your models here.
@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'contact_mail', 'comment', 'user')
    search_fields = ('full_name', 'contact_mail')


@admin.register(Message)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_send', 'periodicity', 'status_code', 'next_send')

