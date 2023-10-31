from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = "delete Clientr by id"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='id of client')      #pk - id

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()                 #поиск строки по id

        if client is not None:
            client.delete()                                            #удаление найденной строки

        self.stdout.write(f'{client}')