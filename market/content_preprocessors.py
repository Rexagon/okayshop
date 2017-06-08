# -*- coding: utf-8 -*-
from market.cart import Cart
from market.models import SiteParameter


def add_site_parameters(request):
    return {
        "parameters": SiteParameter.objects.first()
    }


def add_cart_data(request):
    cart = Cart(request)
    return {
        'cart': cart,
        'num_cart_items': cart.cart.item_set.count()
    }