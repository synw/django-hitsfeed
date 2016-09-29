# -*- coding: utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from hitsfeed.models import UrlTree


@admin.register(UrlTree)
class UrlTreeAdmin(MPTTModelAdmin):
    pass