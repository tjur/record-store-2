# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User
from shop.models import Album, BasketItem, Basket, OrderItem, Order
import django_tables2 as tables
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login_user(request, user)
                return redirect(index)
            else:
                return render(request, "login.html", context={"error": "Konto jest nieaktywne"})
        else:
            return render(request, "login.html", context={"error": "Niepoprawne dane"})
    else:
        return render(request, "login.html")


def logout(request):
    logout_user(request)
    return redirect(index)


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        errors = []
        if not username:
            errors.append("Nie podano nazwy użytkownika")
        elif User.objects.filter(username=username).exists():
            errors.append("Podana nazwa użytkownika jest zajęta")

        if not first_name:
            errors.append("Nie podano imienia")
        if not last_name:
            errors.append("Nie podano nazwiska")

        if not email:
            errors.append("Nie podano adresu email")
        elif User.objects.filter(email=email).exists():
            errors.append("Istnieje już użytkownik o podanym adresie email")

        if not password:
            errors.append("Nie podano hasła")
        elif len(password) < 5:
            errors.append("Za krótkie hasło")
        elif not password_confirm:
            errors.append("Nie podano potwierdzenia hasła")
        elif password != password_confirm:
            errors.append("Podane hasła nie zgadzają się")

        if errors:
            return render(request, "register.html", context={"errors": errors})
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            user = authenticate(username=username, password=password)
            login_user(request, user)
            return redirect(index)
    else:
        return render(request, "register.html")


class AlbumTable(tables.Table):
    cover = tables.Column(orderable=False, verbose_name="")
    id = tables.Column(orderable=False, verbose_name="")

    class Meta:
        model = Album
        fields = ("cover", "name", "artist", "price", "id")
        sequence = ("cover", "name", "artist", "price", "id")
        attrs = {'class': 'table table-striped'}

    def render_cover(self, record):
        return mark_safe('<img width="150" height="150" alt=%s src=%s />' % (escape(record.name), escape(record.cover)))

    def render_price(self, value):
        return mark_safe(u'%s zł' % escape(value))

    def render_id(self, value):
        return mark_safe(('<a class="btn btn-info" href=%s>' % escape(value)) + u'Więcej' + '</a>')


def albums(request):
    table = AlbumTable(Album.objects.all())
    tables.RequestConfig(request, paginate={"per_page": 8}).configure(table)
    return render(request, "albums.html", context={'table': table})


def album_desc(request, album_id):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
    else:
        album = get_object_or_404(Album, pk=album_id)
        return render(request, "album_desc.html", context={"album": album, "range": range(1, min(31, album.quantity + 1))})


def account(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "account.html", context={"user": user})

@login_required
def add_to_basket(request, album_id):
    if request.method == "POST":
        basket_quantity = request.POST.get('basket_quantity')
        album = get_object_or_404(Album, pk=album_id)
        user = request.user

        basket = Basket.objects.filter(user__id=user.id)
        if len(basket) == 0:
            basket = Basket.objects.create(user=user)
            basket.save()
        else:
            basket = basket[0]

        bi = BasketItem.objects.create(basket=basket, album=album, quantity=basket_quantity)
        bi.save()
        table = AlbumTable(Album.objects.all())
        tables.RequestConfig(request, paginate={"per_page": 8}).configure(table)
        return render(request, "albums.html", context={"table": table, "message": "Dodano do koszyka"})
        
    else:
        raise Http404()


def basket(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    basket = Basket.objects.filter(user__id=user.id)
    basket_items = []
    if len(basket) != 0:
        basket_items = BasketItem.objects.filter(basket__id=basket[0].id)

    prices = map(lambda basket_item: basket_item.album.price * basket_item.quantity, basket_items)
    basket_items_and_prices = []
    for i, basket_item in enumerate(basket_items):
        basket_items_and_prices.append({"basket_item": basket_item, "price": prices[i]})

    return render(request, "basket.html", context={"user": user, "amount": sum(prices), "basket_items_and_prices": basket_items_and_prices})

def delete_basket_item(request, user_id, basket_item_id):
    BasketItem.objects.get(pk=basket_item_id).delete()
    return render(request, "index.html", {"message": "Usunięto z koszyka"})


def create_order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    basket = Basket.objects.filter(user__id=user.id)

    if len(basket) == 0:
        raise Http404()

    basket = basket[0]
    basket_items = BasketItem.objects.filter(basket__id=basket.id)
    amount = sum(map(lambda basket_item: basket_item.album.price * basket_item.quantity, basket_items))

    order = Order.objects.create(user=user, amount=amount)
    order.save()

    for basket_item in basket_items:
        order_item = OrderItem.objects.create(order=order, album=basket_item.album, quantity=basket_item.quantity)
        order_item.save()
        Album.objects.filter(id=basket_item.album.id).update(quantity=basket_item.album.quantity-basket_item.quantity)
        BasketItem.objects.get(pk=basket_item.id).delete()

    Basket.objects.get(pk=basket.id).delete()

    return render(request, "index.html", context={"message": "Złożono zamówienie nr " + str(order.id)})


def orders(request, user_id):
    orders = Order.objects.filter(user__id=user_id)
    return render(request, "orders.html", context={"orders": orders})


def contact(request):
    return render(request, "contact.html")