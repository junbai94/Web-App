from django import template

register = template.Library()

@register.filter(name='numloop')
def numloop(num):
    return range(num)

@register.filter(name='index')
def index(l, i):
    return l[i]