from django.shortcuts import render
from django.http import HttpResponse
import logging
from shop_app.models import Client, Order, Product
from datetime import datetime, timedelta
from django.core.files.storage import  FileSystemStorage
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404, redirect


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
                 <li><a href="http://127.0.0.1:8000/shop/product_form/2">изменение продукта на примере с id = 2 с сохранением изображения через форму </a></li>
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
    string = 'Список продуктов:'+ '<br>' + '<br>'
    for product in products:
        string += str(product) + '<br>'
    logger.info(f'Страница "Список продуктов" успешно открыта')
    return HttpResponse(string)


#вывод списка всех клиентов
def clients(request):
    clients = Client.objects.all()
    string = 'Список клиентов:'+ '<br>' + '<br>'
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

def product (request, id_product: int):
    product = Product.objects.filter(pk=id_product).first()
    context = {
        "product": product

    }
    return render(request, "shop_app/product.html", context=context)



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


# представление для ввода данных о продукте через форму и сохранение изображения продукта на сервер
def product_form(request, id_product: int):
    product = get_object_or_404(Product, pk=id_product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.name_product = request.POST["name_product"]
            product.description_product = request.POST["description_product"]
            product.cost = request.POST["cost"]
            product.quantity = request.POST["quantity"]
            image = form.cleaned_data['image']
            #fs = FileSystemStorage()
            #fs.save(image.name, image)                                 #сохранение image на сервер
            if "image" in request.FILES:
                product.image_product = request.FILES["image"]          #запись Image в переменную БД
            product.save()
            logger.info(f"Product {product.name_product} is changed successfully")
            return redirect("product", id_product=product.id)
    else:
        form = ProductForm()

    context = {
        "form": form,
        "product": product,
    }
    return render(request, "shop_app/product_form.html", context=context)


