# -*- coding: utf-8 -*-

from django.shortcuts import render

from market.models import SliderImage


def main(request):
    context = {
        "page": "main",
        "images": SliderImage.objects.all()
    }
    return render(request, 'main.html', context=context)


def products(request):
    context = {
        "page": "products"
    }
    return render(request, 'products.html', context=context)


def services(request):
    context = {
        "page": "services"
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