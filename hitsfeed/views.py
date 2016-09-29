# -*- coding: utf-8 -*-

from django.http.response import Http404
from django.views.generic import TemplateView
from hitsfeed.models import UrlTree


class HitsFeedView(TemplateView):
    template_name = 'hitsfeed/index.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise Http404
        return super(HitsFeedView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(HitsFeedView, self).get_context_data(**kwargs)
        context['nodes'] = UrlTree.objects.all()
        return context