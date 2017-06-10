# -*- coding: utf-8 -*-

import datetime
import models

CART_ID = 'CART-ID'


class ItemAlreadyExists(Exception):
    pass


class ItemDoesNotExist(Exception):
    pass


class Cart:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = models.Cart.objects.get(id=cart_id, checked_out=False)
            except models.Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def new(self, request):
        cart = models.Cart(creation_date=datetime.datetime.now())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product):
        item = models.Item()
        item.cart = self.cart

        item.type = product[u'type']
        item.sheet_type = product[u'sheet_type']
        item.texture = product[u'texture']
        item.square = product[u'square']
        item.coating_main = product[u'coating_main']
        item.coating_additional = product[u'coating_additional']
        item.stained = product[u'stained']

        item.save()

    def remove(self, id):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                id=id
            )
        except models.Item.DoesNotExist:
            # raise ItemDoesNotExist
            pass
        else:
            item.delete()

    def count(self):
        result = 0
        for item in self.cart.item_set.all():
            result += 1
        return result

    def summary(self):
        result = 0
        for item in self.cart.item_set.all():
            result += 0
        return result

    def clear(self):
        for item in self.cart.item_set.all():
            item.delete()
