# -*- coding: utf-8 -*-

from django.contrib import admin

from market.models import SiteParameter, SliderImage, CompositeType


class ParametersAdmin(admin.ModelAdmin):
    fields = ('image_tag', 'logo', 'title', 'email', 'phone', 'about')
    readonly_fields = ('image_tag',)


class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ('name', 'image_tag', 'image')
    readonly_fields = ('image_tag', )


class CompositeTypeAdmin(admin.ModelAdmin):
    fields = ('image_tag', 'logo', 'name', )
    readonly_fields = ('image_tag',)


admin.site.register(SiteParameter, ParametersAdmin)
admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(CompositeType, CompositeTypeAdmin)
