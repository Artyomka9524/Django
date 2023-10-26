from django.shortcuts import render
from django.http import HttpResponse
import logging
from shop_app.models import Client, Order, Product

logger = logging.getLogger(__name__)                # переменная для логирования

def main(request):
    page_main = """
        <div>
            <ul>
                <li><a href="http://127.0.0.1:8000/shop/clients/">список всех клиентов</a></li>
                <li><a href="http://127.0.0.1:8000/shop/products/">список всех товаров</a></li>
                 <li><a href="http://127.0.0.1:8000/shop/orders/">список всех заказов</a></li>
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
    orders = Order.objects.filter(pk=id_order).first()
    return HttpResponse(orders, orders.products)


#вывод списка заказов
def orders(request):
    string = ''
    orders = Order.objects.all()
    for order in orders:
        string += str(order) + '<br>'
    return HttpResponse(string)