# -*- coding: utf-8 -*-

from django.contrib import admin

from market.models import SiteParameter, SliderImage, CompositeType, Service, TexturesGroup, Texture, CompositeSheetType, \
    CompositeSheetOption


class ParametersAdmin(admin.ModelAdmin):
    fields = ('image_tag', 'logo', 'title', 'email', 'phone', 'about')
    readonly_fields = ('image_tag',)


class SliderImageAdmin(admin.ModelAdmin):
    fields = ('name', 'image_tag', 'image')
    readonly_fields = ('image_tag', )


class CompositeTypeAdmin(admin.ModelAdmin):
    fields = ('name', 'image_tag', 'logo', 'short_description', 'full_description', 'application')
    readonly_fields = ('image_tag',)


class ServiceAdmin(admin.ModelAdmin):
    fields = ('name', 'image_tag', 'image', 'short_description', 'full_description', 'order')
    readonly_fields = ('image_tag',)
    ordering = ('order', )


class TextureAdmin(admin.ModelAdmin):
    fields = ('name', 'image_tag', 'image', 'big_image', 'big_image_tag', 'group')
    readonly_fields = ('image_tag', 'big_image_tag')


admin.site.register(SiteParameter, ParametersAdmin)
admin.site.register(SliderImage, SliderImageAdmin)
admin.site.register(CompositeType, CompositeTypeAdmin)
admin.site.register(CompositeSheetType)
admin.site.register(CompositeSheetOption)
admin.site.register(Service, ServiceAdmin)
admin.site.register(TexturesGroup)
admin.site.register(Texture, TextureAdmin)
