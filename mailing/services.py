from datetime import datetime
import os


from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django.utils import timezone

from mailing.models import Logs, Mailing


def send_mailing(mailing):
    print(f'Send mail: {datetime.now().time()}')
    subject = mailing.message_id.title
    message = mailing.message_id.text
    from_email = os.getenv('EMAIL_HOST_USER')
    recipient_list = [client.contact_mail for client in mailing.client_id.all()]
    for recipient in recipient_list:
        response = send_mail(subject, message, from_email, [recipient])
        if response == 1:
            status = 'Отправленно'
            server_response = 'Рассылка успешно отправленна!'
        else:
            status = 'Ошибка отправки'
            server_response = 'Рассылка не отправленна, информацию уточняйте у администратора платформы!'
        log = Logs(date_time=timezone.now(), status=status, server_response=server_response,
                   mailings_id=mailing, user=mailing.user)
        log.save()


def check_mailing():
    now = timezone.now()
    mailings = Mailing.objects.filter(status_code='create', time_send__lte=now.time(), next_send__lte=now.date())
    for mail in mailings:
        send_mailing(mail)
        mail.start_mailing()


def start_apscheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_mailing, 'interval', minutes=1, id='run_mailing', replace_existing=True, jobstore='default')
    scheduler.start()
