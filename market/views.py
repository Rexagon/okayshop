# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from market.models import SliderImage, Service, CompositeType


def main(request):
    context = {
        "page": "main",
        "images": SliderImage.objects.all(),
        "composites": CompositeType.objects.all()
    }
    return render(request, 'main.html', context=context)


def products(request):
    context = {
        "page": "products",
        "composites": CompositeType.objects.all()
    }
    return render(request, 'products.html', context=context)


def composite(request, name=""):
    try:
        product = CompositeType.objects.filter(name__iexact=name)[0]
        context = {
            "page": "products",
            "composite": product
        }
        return render(request, "composite.html", context=context)
    except IndexError:
        return redirect('/products')


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