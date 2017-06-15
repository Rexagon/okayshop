from django.conf.urls import url

from market.views import main, products, services, delivery, checkout, contacts, order, message, handle_order, \
    handle_order_remove

urlpatterns = [
    url(r'^$', main, name="main"),
    url(r'^products/(?P<name>\w+)/?$', products, name="composite"),
    url(r'^products/(?P<name>\w+)/order/?$', order, name="order"),
    url(r'^order/?$', handle_order, name="handle_order"),
    url(r'^order/remove/(?P<id>\d+)/?$', handle_order_remove, name="handle_order_remove"),
    url(r'^services/?$', services, name="services"),
    url(r'^delivery/?$', delivery, name="delivery"),
    url(r'^checkout/?$', checkout, name="checkout"),
    url(r'^checkout/order/?$', handle_checkout, name="handle_checkout"),
    url(r'^contacts/?$', contacts, name="contacts"),

    #stuff urls
    url(r'^message/?$', message)
]


