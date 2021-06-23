"""
自定义过滤器实现的方法:
https://docs.djangoproject.com/zh-hans/3.1/howto/custom-template-tags/
"""
from django import template
from datetime import  datetime
register = template.Library()

@register.filter(name='timefmt')
def timefmt(value):
    """将时间戳转换成datetime类型的时间"""
    return datetime.fromtimestamp(value)

@register.filter(name='cpu_val_fmt')
def cpu_val_fmt(value):
    return  round(value/1000, 2)