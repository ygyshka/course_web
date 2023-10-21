from django.core.management import BaseCommand

from mailing.models import Clients


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {"contact_mail": "test@yandex.ru", "full_name": "Metuy MacConest", "comment": "Person from Canada"},
            {"contact_mail": "test@gmail.com", "full_name": "Genree Bishop Flower", "comment": "Person from Mexico"},
            {"contact_mail": "test@mail.ru", "full_name": "Alex Bruno Mackendi", "comment": "Person from america"}
        ]
        # для меньшей нагрузки подключения к бд лучше использовать такой метод передачи данных к модели
        # с дальнейшей записью в бд, в противном случае если идти через цикл по списку и кажэдый item
        # по одному записывать в бд, будет большое количество подключений и это нагрузит бд

        category_for_create = []
        for item in category_list:
            category_for_create.append(
                Clients(**item)
            )
        # Очищение таблици перед записью новых данных
        # (ньанс только в том, что не понимаю почему айдишники инкрементируются)
        Clients.objects.all().delete()

        Clients.objects.bulk_create(category_for_create)
