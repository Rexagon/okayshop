# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe


class SiteParameter(models.Model):
    logo = models.ImageField(verbose_name="Логотип")
    title = models.CharField(max_length=128, verbose_name="Название")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=32, verbose_name="Номер телефона")
    about = models.TextField(verbose_name="О нас")

    def image_tag(self):
        return mark_safe('<img src="/static/media/%s"/>' % self.logo)

    image_tag.short_description = "Логотип(просмотр)"

    class Meta:
        verbose_name = "параметр"
        verbose_name_plural = "Параметры"

    def __unicode__(self):
        return "Глобальная информация"


class SliderImage(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    image = models.ImageField(verbose_name="Изображение")

    def image_tag(self):
        return mark_safe('<img src="/static/media/%s" height="200" />' % self.image)

    image_tag.short_description = "Изображение(просмотр)"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Слайдер"

    def __unicode__(self):
        return self.name


class CompositeType(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    logo = models.ImageField(verbose_name="Логотип")
    short_description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(verbose_name="Описание")

    def image_tag(self):
        return mark_safe('<img src="/static/media/%s" height="84" />' % self.logo)

    image_tag.short_description = "Логотип(просмотр)"

    class Meta:
        verbose_name = "композит"
        verbose_name_plural = "Композиты"

    def __unicode__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    short_description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", blank=True)
    order = models.IntegerField(verbose_name="Порядок")

    def image_tag(self):
        return mark_safe('<img src="/static/media/%s" height="200" />' % self.image)

    image_tag.short_description = "Изображение(просмотр)"

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "Услуги"

    def __unicode__(self):
        return self.name
