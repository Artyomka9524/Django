from django.core.management.base import BaseCommand
from shop_app.models import Client, Order, Product


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument("id_client", type=int, help="client ID")
        parser.add_argument('-p', '--id_product', nargs='+', help="client ID", required=True)

    def handle(self, *args, **kwargs):
        id_client = kwargs.get('id_client')
        id_product: list = kwargs.get('id_product')                         #запись в id_product  параметров из командной строки

        client = Client.objects.filter(pk=id_client).first()

        order = Order(buyer=client)
        total_price = 0
        for i in range(0, len(id_product)):
            product = Product.objects.filter(pk=id_product[i]).first()
            total_price += float(product.cost)
            order.total_cost = total_price
            order.save()
            order.products.add(product)











# class Command(BaseCommand):
#     help = "create order "
#
#     def add_arguments(self, parser):
#
#         parser.add_argument('id_client', type=int, help='client id')                 # выбираем клиента для составления закааз
#         parser.add_argument('-p', '--Product_id', nargs='+', help="User ID", required=True)
#
#     def handle(self, *args, **kwargs):
#         id_client = kwargs.get('id_client')
#         client = User.objects.filter(pk=id_client).first()                          #получение Client по id
#         order = Order(buyer=client)                                                 # по ключу ID client в поле Buyer  связываем табл Order  с табл Client
#         order.save()
#
#         self.stdout.write(f'{client}')                             #выводит в формате прописанном в __str__ в models.py
#
# class Order(models.Model):
#     buyer = models.ForeignKey(Client, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)                                              #создается автоматически таблица Order_product связи табдиц Order и Product
#     total_cost = models.DecimalField(max_digits=8, decimal_places=2)
#     date_create_order = models.DateField(auto_now_add=True)