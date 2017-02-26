# -*- coding: utf-8 -*-

from django.contrib import admin

from market.models import SiteParameter, SliderImage, CompositeType, Service


class ParametersAdmin(admin.ModelAdmin):
    fields = ('image_tag', 'logo', 'title', 'email', 'phone', 'about')
    readonly_fields = ('image_tag',)


class SliderImageAdmin(admin.ModelAdmin):
    fields = ('name', 'image_tag', 'image')
    readonly_fields = ('image_tag', )


class CompositeTypeAdmin(admin.ModelAdmin):
    fields = ('name', 'image_tag', 'logo', 'short_description', 'full_description')
    readonly_fields = ('image_tag',)


class ServiceAdmin(admin.ModelAdmin):
    fields = ('name', 'image_tag', 'image', 'short_description', 'full_description', 'order')
    readonly_fields = ('image_tag',)
    ordering = ('order', )


admin.site.register(SiteParameter, ParametersAdmin)
admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(CompositeType, CompositeTypeAdmin)
admin.site.register(Service, ServiceAdmin)
