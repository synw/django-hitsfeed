# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import TreeForeignKey, MPTTModel


class UrlTree(MPTTModel):
    url = models.CharField(max_length=200, verbose_name=_(u"Url"))
    parent = parent = TreeForeignKey('self', null=True, blank=True, related_name=u'children', verbose_name=_(u'Parent url'))
    
    class Meta:
        verbose_name=_(u'Url tree')
        verbose_name_plural = _(u'Urls tree')
        ordering = ('url',)

    def __unicode__(self):
        return unicode(self.url)