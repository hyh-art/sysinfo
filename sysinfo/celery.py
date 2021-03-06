from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# 设置django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sysinfo.settings')
app = Celery('sysinfo')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()# 发现任务文件每个app下的task.py


