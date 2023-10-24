from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone

from mailing import constants


# Create your models here.


class Clients(models.Model):

    contact_mail = models.EmailField(max_length=150,
                                     verbose_name='контактный Email')
    full_name = models.CharField(max_length=200,
                                 verbose_name='Ф.И.О.')
    comment = models.TextField(verbose_name='коментарий', **constants.NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL
                             , on_delete=models.SET_NULL,
                             **constants.NULLABLE,
                             verbose_name='создатель')

    def __str__(self):
        return f'{self.contact_mail} {self.full_name} {self.comment}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailing(models.Model):

    time_send = models.TimeField(verbose_name='время рассылки')
    periodicity = models.CharField(max_length=50,
                                   choices=constants.PERIODICITY,
                                   verbose_name='переодичность')
    status_code = models.CharField(max_length=50, default=constants.STATUS_CREATE,
                                   choices=constants.STATUS_CODE,
                                   verbose_name='статус рассылки')
    client_id = models.ManyToManyField('Clients', verbose_name='клиенты')
    next_send = models.DateField(verbose_name='дата следующей отправки')

    message_id = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='Сообщения')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **constants.NULLABLE)

    def __str__(self):
        return f'{self.time_send} {self.periodicity} {self.status_code}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    def start_mailing(self):
        # Меняем статус рассылки
        self.status_code = constants.STATUS_ACTIVE
        self.save()
        # Обновляем дату следующего запуска
        if self.periodicity == constants.DAILY:
            self.next_send += timedelta(days=1)
        elif self.periodicity == constants.WEEKLY:
            self.next_send += timedelta(weeks=1)
        elif self.periodicity == constants.MONTHLY:
            self.next_send += timedelta(days=30)

        if self.next_send > timezone.now().date():
            self.status_code = constants.STATUS_CREATE
        else:
            self.status_code = constants.STATUS_ACTIVE
        self.save()


class Message(models.Model):

    title = models.CharField(max_length=150, verbose_name='тема письма', **constants.NULLABLE)
    text = models.TextField(verbose_name='тело письма', **constants.NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **constants.NULLABLE)

    def __str__(self):
        return f'{self.title} {self.text}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Logs(models.Model):

    date_time = models.DateTimeField()
    status = models.CharField()
    server_response = models.CharField(max_length=200) #= результат отработки функции send_mail()
                                                  # два варианта, либо все хорошо, либо плохо и в поле
                                                  # записывать ошибку с ее обозначением, дулать через try\except
                                                  # except Exception as e: status = e мб e.__srt__ (как пример)
    mailings_id = models.ForeignKey('Mailing', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **constants.NULLABLE)

    def __str__(self):
        return f'{self. date_time} {self.server_response}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
