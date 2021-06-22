# -*- coding: utf-8 -*-
# @Time:  2021/6/22 20:26
# @Author :hyh
# @File: timefilter
from django import template
from datetime import datetime
register=template.Library()

@register.filter(name='timefmt')
def timefmt(value):
    return datetime.fromtimestamp(value)