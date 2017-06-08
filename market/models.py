# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.template.defaulttags import register
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
    application = models.TextField(verbose_name='Применение')

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


class TexturesGroup(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')

    @property
    def textures(self):
        return Texture.objects.filter(group_id__exact=self.id)

    class Meta:
        verbose_name = "группа текстур"
        verbose_name_plural = "Группы текстур"

    def __unicode__(self):
        return self.name


class Texture(models.Model):
    name = models.CharField(max_length=128, verbose_name="Артикул")
    image = models.ImageField(verbose_name="Изображение")
    big_image = models.ImageField(verbose_name="Большое изображение")
    group = models.ForeignKey('TexturesGroup', on_delete=models.CASCADE)

    def image_tag(self):
        return mark_safe('<img src="/static/media/%s" height="200" />' % self.image)

    def big_image_tag(self):
        return mark_safe('<img src="/static/media/%s" height="200" />' % self.big_image)

    class Meta:
        verbose_name = "текстура"
        verbose_name_plural = "Текстуры"

    def __unicode__(self):
        return self.name


class CompositeSheetType(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    width = models.IntegerField(verbose_name="Ширина")
    length = models.IntegerField(verbose_name="Длина")
    thickness = models.IntegerField(verbose_name="Толщина")
    composite_type = models.ForeignKey('CompositeType', on_delete=models.CASCADE)
    price_low = models.DecimalField(verbose_name="Стоимость (р/м2)", max_digits=10, decimal_places=2)
    price_middle = models.DecimalField(verbose_name="Стоимость (р/м2)от 100 м2 до 500 м2", max_digits=10, decimal_places=2)
    price_high = models.DecimalField(verbose_name="Стоимость (р/м2) от 500 м2", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "вид панели"
        verbose_name_plural = "Виды панелей"

    def __unicode__(self):
        return self.name


class CompositeSheetOption(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(verbose_name="Краткое описание")

    class Meta:
        verbose_name = "опция панели"
        verbose_name_plural = "Опции панели"

    def __unicode__(self):
        return self.name
