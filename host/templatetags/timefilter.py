from django import template
from datetime import  datetime
register = template.Library()

@register.filter(name='timefmt')
def timefmt(value):
    """将时间戳转换成datetime类型的时间"""
    return datetime.fromtimestamp(value)

@register.filter(name='cpu_val_fmt')    ##添加的自定义过滤器
def cpu_val_fmt(value):
    return  round(value/1000, 2)