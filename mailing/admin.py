from django.contrib import admin

from mailing.models import Clients, Message


# Register your models here.
@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'contact_mail', 'comment')
    search_fields = ('full_name', 'contact_mail')


@admin.register(Message)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
