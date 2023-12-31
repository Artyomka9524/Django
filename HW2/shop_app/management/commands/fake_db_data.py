from django.core.management.base import BaseCommand
from shop_app.models import Product, Client, Order
import random

class Command(BaseCommand):
    help = "Generate fake clients"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='quantity of fake clients')


    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        name = ['Андрей', 'Кирилл', 'Матвей', 'Дмитрий', 'Даниил', 'Максим',  'Артём', 'Александр', 'Анастасия', 'Дарья', 'Мария', 'Виктория',  'Екатерина', 'Ксения']
        clients_ = []
        products_ = []
        orders_ = []

        for i in range(1, count + 1):
            client = Client(name_client=f'{random.choice(name)}',
                            email=f'email{i}@mail.ru',
                            phone_number=f'{random.randint(89510000000, 89518888888)}',
                            address=f'address{i}')
            client.save()
            clients_.append(client)

        # формируем 20 товаров
        pr = 20
        for j in range(1, pr):
            product = Product(name_product=f'product{j}',
                            description_product=f'description{j}',
                            cost=f'{random.randint(1,100)}.{random.randint(1,100)}',
                            quantity=f'{random.randint(1, 20)}',
                            date_add_product = f'27-0-2023')
            product.save()
            products_.append(product)

        #формируем 10 заказов
        total_cost = 0
        for k in range(1, 10):
            order = Order(buyer=clients_[random.randint(0, count-1)])
            for m in range(0, pr-1):
                if random.randint(0, 1) == 1:
                    total_cost += float(products_[m].cost)
                    order.total_cost = total_cost
                    order.save()
                    order.products.add(products_[m])                    # добавление товара в заказ



