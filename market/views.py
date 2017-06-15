# -*- coding: utf-8 -*-
import json
from decimal import Decimal

from django.http import JsonResponse
from django.shortcuts import render, redirect
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

            gradations = []
            if sheet_type.price_huge:
                gradations = [500, 1000, 3000]
            else:
                gradations = [100, 500, 1000]

            if square < gradations[0]:
                price += sheet_type.price_low
            elif gradations[0] <= square < gradations[1]:
                price += sheet_type.price_middle
            elif gradations[1] <= square < gradations[2]:
                price += sheet_type.price_high
            else:
                price += sheet_type.price_huge

            composite['price'] = price
            composite['total'] = Decimal(square) * price
            total += composite['total']
            composite['texture'] = Texture.objects.get(id=item.texture).name
            composite['coatings'] = coatings
            composite['sheet_type'] = sheet_type
            composite['square'] = square
            composites.append(composite)

    context = {
        "page": "checkout",
        "cart": cart,
        "total": total,
        "composites": composites
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
    if request.method == "POST"
        cart = Cart(request)
        cart.clear()
        return JsonResponse({})


@csrf_exempt
def message(request):
    if request.method == "POST":

        return JsonResponse({})
    else:
        return redirect('/')
