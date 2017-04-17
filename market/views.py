# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from market.models import SliderImage, Service, CompositeType, CompositeSheetType, TexturesGroup


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
    context = {
        "page": "checkout"
    }
    return render(request, 'checkout.html', context=context)


def contacts(request):
    context = {
        "page": "contacts"
    }
    return render(request, 'contacts.html', context=context)


# stuff functions

@csrf_exempt
def message(request):
    if request.method == "POST":

        return JsonResponse({})
    else:
        return redirect('/')
