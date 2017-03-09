from django.conf.urls import url

from market.views import main, products, services, delivery, checkout, contacts, order, message

urlpatterns = [
    url(r'^$', main, name="main"),
    url(r'^products/(?P<name>\w+)/?$', products, name="composite"),
    url(r'^products/(?P<name>\w+)/order/?$', order, name="order"),
    url(r'^services/?$', services, name="services"),
    url(r'^delivery/?$', delivery, name="delivery"),
    url(r'^checkout/?$', checkout, name="checkout"),
    url(r'^contacts/?$', contacts, name="contacts"),

    #stuff urls
    url(r'^message/?$', message)
]


