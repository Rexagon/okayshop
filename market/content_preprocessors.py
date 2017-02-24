# -*- coding: utf-8 -*-
from market.models import SiteParameter


def add_site_parameters(request):
    return {
        "parameters": SiteParameter.objects.first()
    }
