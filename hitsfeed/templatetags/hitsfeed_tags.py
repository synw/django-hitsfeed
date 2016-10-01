# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from hitsfeed.models import UrlTree


register = template.Library()

def recurse_nodes(node, lvl=0, prev_lvl=0):
    output = ''
    if lvl == 0:
        output = '<ul>'
        output += '\t<li><a href="#">'+str(node.url)+'</a></li>\n'
    for descendant in node.get_children():
        lvl_n = lvl+1
        output+='\n<li>'+recurse_nodes(descendant, lvl_n, lvl)+'</li>\n'
    if lvl == 0:
        output += '</ul>'
    return output

@register.simple_tag()
def get_tree():
    root_node = UrlTree.objects.get(url='/')
    output = '<div class="tree">\n'+recurse_nodes(root_node)+'\n</div>'
    return mark_safe(output)

@register.filter
@stringfilter
def get_id_from_url(url):
    xid = url.replace('/','---')
    return xid