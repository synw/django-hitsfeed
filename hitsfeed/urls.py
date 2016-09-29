# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.conf.urls import url
from django.views.generic import RedirectView
from hitsfeed.views import HitsFeedView


urlpatterns = [
    url(r'^', HitsFeedView.as_view(), name="hitsfeed-index")
]
