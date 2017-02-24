from django.conf.urls import url

from market.views import main, products, services, delivery, checkout, contacts

urlpatterns = [
    url(r'^$', main, name="main"),
    url(r'^products/?', products, name="products"),
    url(r'^services/?', services, name="services"),
    url(r'^delivery/?', delivery, name="delivery"),
    url(r'^checkout/?', checkout, name="checkout"),
    url(r'^contacts/?', contacts, name="contacts")
]
