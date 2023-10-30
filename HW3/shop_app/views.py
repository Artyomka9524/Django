from django.shortcuts import render
from django.http import HttpResponse
import logging
from shop_app.models import Client, Order, Product
# import datetime
# from datetime import date
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)                # переменная для логирования

def main(request):
    page_main = """
        <div>
            <ul>
                <li><a href="http://127.0.0.1:8000/shop/clients/">список всех клиентов</a></li>
                <li><a href="http://127.0.0.1:8000/shop/products/">список всех товаров</a></li>
                 <li><a href="http://127.0.0.1:8000/shop/orders/">список всех заказов</a></li>
                 <li><a href="http://127.0.0.1:8000/shop/client_orders/5">список всех заказов  на примере клиента id=5</a></li>
                 <li><a href="http://127.0.0.1:8000/shop/client_products_sorted/4/1">список отсортированных товаров за последние 1 день на примере клиента id=4</a></li>
            </ul>
        </div>
        <form action='http://127.0.0.1:8000/' target="_blank">
            <button>Начальная страница</button>
        </form>
        <br>
        <footer>
            <div>
                <p> Контакты: Россия, Воронеж, ул. Люзикова</p>
            </div>
        </footer>
        """
    logger.info(f'Страница "Главная" успешно открыта')

    return HttpResponse(page_main)


# вывод всех товаров
def products(request):
    products = Product.objects.all()                        #получение данных из табл Product  БД
    string = ''
    for product in products:
        string += str(product) + '<br>'
    logger.info(f'Страница "Список продуктов" успешно открыта')
    return HttpResponse(string)


#вывод списка всех клиентов
def clients(request):
    clients = Client.objects.all()
    string = ''
    for client in clients:
       string += str(client) + '<br>'
    logger.info(f'Страница "Список клиентов" успешно открыта')
    return HttpResponse(string)


# вывод заказа по  id
def order(request, id_order: int):
    #order = Order.objects.filter(pk=id_order).first()
    order = Order.objects.get(pk=id_order)
    context = {
        'order': order
    }
    return render(request, 'shop_app/order.html', context=context)


#вывод списка заказов
def orders(request):
    orders = Order.objects.all()
    for order in orders:
        print (order.id)
    context = {
        'orders': orders
    }
    return render(request, 'shop_app/orders_all.html', context=context)


def client_orders(request, id_client: int):
    products = {}

    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(buyer=client).all()

    for order in orders:
        products[order.id] = str(order.products.all()).replace('<QuerySet [<', '').replace('>]>', '').split('>, <')


    return render(request, 'shop_app/client_orders.html', {'client': client, 'orders': orders, 'products': products})


def client_products_sorted(request, id_client: int, days: int):
    products = []
    product_set=[]
    now = datetime.now()
    before = now - timedelta(days=days)
    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(buyer=client, date_create_order__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'shop_app/client_all_products_from_orders.html', {'client': client, 'product_set': product_set, 'days': days})