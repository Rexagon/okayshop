# -*- coding: utf-8 -*-
import json
from decimal import Decimal

from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from math import ceil

from market.cart import Cart
from market.models import SliderImage, Service, CompositeType, CompositeSheetType, TexturesGroup, Texture


def main(request):
    context = {
        "page": "main",
        "images": SliderImage.objects.all(),
        "composites": CompositeType.objects.all()
    }
    return render(request, 'main.html', context=context)


def products(request, name=""):
    try:
        product = CompositeType.objects.filter(name__iexact=name)[0]
        context = {
            "page": "products_" + product.name.lower(),
            "composite": product
        }
        return render(request, "products.html", context=context)
    except IndexError:
        return redirect('/')


def order(request, name=""):
    try:
        product = CompositeType.objects.filter(name__iexact=name)[0]
        sheet_types = CompositeSheetType.objects.filter(composite_type__name__iexact=name)
        texture_groups = TexturesGroup.objects.all()
        context = {
            "page": "products_" + product.name.lower(),
            "composite": product,
            "sheet_types": sheet_types,
            "texture_groups": texture_groups
        }
        return render(request, "order.html", context=context)
    except IndexError:
        return redirect('/')


@csrf_exempt
def handle_order(request):
    if request.method == 'POST':
        try:
            cart = Cart(request)

            data = json.loads(request.body)

            cart.add(data)

            return JsonResponse({})
        except:
            return JsonResponse({'err': True})


def services(request):
    context = {
        "page": "services",
        "services": Service.objects.all().order_by('order')
    }
    return render(request, 'services.html', context=context)


def delivery(request):
    context = {
        "page": "delivery"
    }
    return render(request, 'delivery.html', context=context)


def checkout(request):
    cart = Cart(request)

    composites = []
    services = []
    total = 0
    for item in cart:
        if item.type == 1 or item.type == 2:
            composite = dict()
            composite['id'] = item.id

            price = 0
            coatings = ''
            if item.coating_main == 1:
                coatings += u'Покрытие PE'
                price += 0
            else: # item.coating_main == 2:
                coatings += u'Покрытие PVDF'
                price += 70

            if item.coating_additional != 0:
                coatings += u',<br>'
                if item.coating_additional == 1:
                    coatings += u'Текстурное покрытие на основе УФ-отверждаемых полимеров'
                    price += 500
                elif item.coating_additional == 2:
                    coatings += u'Текстурное покрытие на основе ПЭТ'
                    price += 350
                elif item.coating_additional == 3:
                    coatings += u'Крашеное покрытие'
                    price += 200

            item_texture = Texture.objects.get(id=item.texture)
            if item_texture.name == 'GRC-0005 brushed':
                coatings += u',<br>Цвет "Царапаное серебро"'
                price += 300
            elif item_texture.name == 'GRC-0007 silver mirror' or item_texture.name == 'GRC-0008 gold mirror':
                coatings += u',<br>Зеркальное покрытие'
                price += 750

            if item.stained:
                coatings += u',<br>'
                if item.coating_additional != 0:
                    coatings += u'Покрытие лаком'
                else:
                    coatings += u'Глянец'
                price += 150

            sheet_type = CompositeSheetType.objects.get(id=item.sheet_type)
            square = item.square

            sheet_square = sheet_type.width * sheet_type.length / 1000000.0
            sheet_count = int(ceil(square / sheet_square))
            square = sheet_square * sheet_count

            titles = ['лист', 'листа', 'листов']
            cases = [2, 0, 1, 1, 1, 2]
            sheet = titles[2 if 4 < sheet_count % 100 < 20 else cases[sheet_count % 10 if sheet_count % 10 < 5 else 5]]

            gradations = [100, 500, 1000, 3000]

            if square < gradations[0]:
                price += sheet_type.price_low
            elif gradations[0] <= square < gradations[1]:
                price += sheet_type.price_middle
            elif gradations[1] <= square < gradations[2]:
                price += sheet_type.price_high
            else:
                price += sheet_type.price_huge

            composite['price'] = price
            composite['total'] = float("{0:.2f}".format((Decimal(square) * price)))
            total += composite['total']
            composite['texture'] = item_texture
            composite['coatings'] = coatings
            composite['sheet_type'] = sheet_type
            composite['square'] = square
            composite['sheet_count'] = str(sheet_count) + ' ' + sheet
            composites.append(composite)

    context = {
        "page": "checkout",
        "cart": cart,
        "total": total,
        "composites": composites,
        "services": Service.objects.all()
    }
    return render(request, 'checkout.html', context=context)


def handle_order_remove(request, id):
    cart = Cart(request)
    cart.remove(id)
    return redirect('/checkout/')


def contacts(request):
    context = {
        "page": "contacts"
    }
    return render(request, 'contacts.html', context=context)


# stuff functions

@csrf_exempt
def handle_checkout(request):
    if request.method == "POST":
        cart = Cart(request)

        try:
            contact_person = escape(request.POST[u'contact_person'])
            email = escape(request.POST[u'email'])
            phone = escape(request.POST[u'phone'])

            company = escape(request.POST[u'company'])

            inn = u''
            if u'inn' in request.POST:
                inn = escape(request.POST[u'inn'])

            address = u''
            if u'address':
                address = escape(request.POST[u'address'])

            message = u''
            if u'message' in request.POST:
                message = request.POST[u'message']

            text = u'Название компании: ' + company + u'<br>'
            text += u'Юридический адрес: ' + address + u'<br>'
            text += u'ИНН: ' + inn + u'<br>'
            text += u'Контактное лицо: ' + contact_person + u'<br>'
            text += u'E-mail: ' + email + u'<br>'
            text += u'Телефон: ' + phone + u'<br>'
            text += u'Доп. информация: ' + message + u'<hr><br>'
            text += u'<table border="1">\
                 <thead>\
                    <tr>\
                        <th>Тип листа</th>\
                        <th>Покрытия</th>\
                        <th>Текстура</th>\
                        <th>Площадь*, м&sup2;</th>\
                        <th style="min-width: 120px">Цена за м&sup2;, руб.</th>\
                        <th style="min-width: 120px">Всего, руб.</th>\
                    </tr>\
                </thead>\
                <tbody>'

            cart = Cart(request)
            services = []
            total = 0
            for item in cart:
                if item.type == 1 or item.type == 2:
                    composite = dict()
                    composite['id'] = item.id

                    price = 0
                    coatings = ''
                    if item.coating_main == 1:
                        coatings += u'Покрытие PE'
                        price += 0
                    elif item.coating_main == 2:
                        coatings += u'Покрытие PVDF'
                        price += 70

                    if item.coating_additional != 0:
                        coatings += u',<br>'
                        if item.coating_additional == 1:
                            coatings += u'Текстурное покрытие на основе УФ-отверждаемых полимеров'
                            price += 500
                        elif item.coating_additional == 2:
                            coatings += u'Текстурное покрытие на основе ПЭТ'
                            price += 350
                        elif item.coating_additional == 3:
                            coatings += u'Крашеное покрытие'
                            price += 200

                    item_texture = Texture.objects.get(id=item.texture)
                    if item_texture.name == 'GRC-0005 brushed':
                        coatings += u',<br>Цвет "Царапаное серебро"'
                        price += 300
                    elif item_texture.name == 'GRC-0007 silver mirror' or item_texture.name == 'GRC-0008 gold mirror':
                        coatings += u',<br>Зеркальное покрытие'
                        price += 750

                    if item.stained:
                        coatings += u',<br>'
                        if item.coating_additional != 0:
                            coatings += u'Покрытие лаком'
                        else:
                            coatings += u'Глянец'
                        price += 150

                    sheet_type = CompositeSheetType.objects.get(id=item.sheet_type)
                    square = item.square

                    sheet_square = sheet_type.width * sheet_type.length / 1000000.0

                    square = sheet_square * ceil(square / sheet_square)

                    gradations = [100, 500, 1000, 3000]

                    if square < gradations[0]:
                        price += sheet_type.price_low
                    elif gradations[0] <= square < gradations[1]:
                        price += sheet_type.price_middle
                    elif gradations[1] <= square < gradations[2]:
                        price += sheet_type.price_high
                    else:
                        price += sheet_type.price_huge

                    composite['price'] = price
                    composite['total'] = float(u"{0:.2f}".format((Decimal(square) * price)))
                    total += composite['total']
                    composite['texture'] = Texture.objects.get(id=item.texture)
                    composite['coatings'] = coatings
                    composite['sheet_type'] = sheet_type
                    composite['square'] = square

                    text += u'<tr>\
                        <td>\
                            <p>' + str(sheet_type).decode('utf8') + u'</p>\
                        </td>\
                        <td>\
                            <p>' + coatings + u'</p>\
                        </td>\
                        <td>\
                            <p><img style="width: 50px; float: left; margin-right: 8px;" src="http://aluminiumcomposite.ru/static/media/' + composite['texture'].image.name.decode('utf8') + u'"> ' + composite['texture'].name.decode('utf8') + u'</p>\
                        </td>\
                        <td>\
                            <p>' + str(composite['square']).decode('utf8') + u' (' + str(item.square).decode('utf8') + u') [' + str(ceil(square / sheet_square)).decode('utf-8') + u' листов]</p>\
                        </td>\
                        <td>\
                            <p>' + str(price).decode('utf8') + u'</p>\
                        </td>\
                        <td>\
                            <p>' + str(composite['total']).decode('utf8') + u'</p>\
                        </td>\
                    </tr>'

            text += u'<tr><td colspan="4"></td><td>Итого:</td><td>' + str(total).decode('utf8') + u' руб.</td><tbody></table><br>'

            if u'services[]' in request.POST and len(request.POST.getlist(u'services[]')) > 0:
                print request.POST.getlist(u'services[]')
                text += u'<br><b>Услуги:</b><br>'
                for service_id in request.POST.getlist(u'services[]'):
                    try:
                        service = Service.objects.get(id=int(service_id))
                        text += u'&nbsp;&nbsp;&nbsp;&nbsp;' + service.name + u'<br>'
                    except:
                        pass

            msg = EmailMessage(u'Заказ', text, 'mailer@live-to-create.com',
                                   ['info@okay-agency.ru'])
            msg.content_subtype = "html"
            if msg.send() > 0:
                cart.clear()
                return JsonResponse({})
            else:
                raise Exception
        except:
            return JsonResponse({'err': True})
    else:
        return redirect('/')


@csrf_exempt
def message(request):
    if request.method == "POST":
        try:
            name = escape(request.POST[u'name'])
            email = escape(request.POST[u'email'])
            message = escape(request.POST[u'message'])

            text = u'Имя: ' + name + u'<br>E-mail: ' + email + u'<hr>Сообщение: ' + message + u'<br><br>'

            msg = EmailMessage(u'aluminiumcomposite.ru | Вопрос', text, 'mailer@live-to-create.com',
                               ['info@okay-agency.ru'])

            msg.content_subtype = "html"
            if msg.send() > 0:
                return JsonResponse({})
            else:
                raise Exception
        except:
            return JsonResponse({'err': True})
    else:
        return redirect('/')
