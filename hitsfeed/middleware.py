# -*- coding: utf-8 -*-

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object
from instant.producers import broadcast
    
    
class HitsFeedMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path == '/hits/':
            return response
        if request.is_ajax():
            return response
        data = {}
        data["path"] = request.path
        data["method"] = request.method
        data['ip'] = request.META['REMOTE_ADDR']
        data['user_agent'] = request.META['HTTP_USER_AGENT']
        data['referer'] = ''
        if data.has_key('HTTP_REFERER'):
            data['referer'] = request.META['HTTP_REFERER']
        data['user'] = 'Anonymous'
        if request.user.is_authenticated():
            data['user'] = request.user.username 
        broadcast(message="Hit", event_class="__hit__", data=data, target="staff")
        return response