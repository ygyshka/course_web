from django.core.management import BaseCommand

from mailing.services import check_mailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        check_mailing()
