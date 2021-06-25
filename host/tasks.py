import psutil
from celery import shared_task
from host.models import UserCpuPercent
@shared_task()   ##装饰器共享任务
def scan_cpu_info():   #扫描cpu
    percent = UserCpuPercent( user_percent=psutil.cpu_times_percent().user)   ##获取用户占用cpu百分比
    percent.save()