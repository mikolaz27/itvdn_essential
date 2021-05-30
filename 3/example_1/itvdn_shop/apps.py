from django.apps import AppConfig


class ItvdnShopConfig(AppConfig):
    name = 'itvdn_shop'


from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
