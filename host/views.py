import platform

from django.shortcuts import render
import psutil
import datetime
import os,platform
# Create your views here.
from host.models import UserCpuPercent


def index(request):
    try:
        info=os.uname()
    except Exception as e:
        info=platform.uname()
    sys_name=info.node
    kernel_name=info.system
    kernel_no=info.release
    kernel_version=info.version
    sys_framework=info.machine
   # boot_time= psutil.boot_time()
   # now_time= datetime.datetime.now()
   # up_time=now_time-boot_time
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    boot_time_format = boot_time.strftime("%Y-%m-%d %H:%M:%S")
    now_time = datetime.datetime.now()
    now_time_format = now_time.strftime("%Y-%m-%d %H:%M:%S")
    up_time = "{} 天 {} 小时 {} 分钟 {} 秒".format(
        (now_time - boot_time).days,
        str(now_time - boot_time).split('.')[0].split(':')[0],
        str(now_time - boot_time).split('.')[0].split(':')[1],
        str(now_time - boot_time).split('.')[0].split(':')[2]
    )
    return render(request,'host/index.html',locals())

def user(request):
    users=psutil.users()
    return render(request,'host/user.html',locals())

def cpu(request, chart=None):
    logical_core_num = psutil.cpu_count()  #
    physical_core_num = psutil.cpu_count(logical=False)
    try:
        load_avg = os.getloadavg()
    except Exception as e:
        load_avg = ['', '', '']
    cpu_time_percent = psutil.cpu_times_percent()
    else_percent = 0.0
    for i in range(3, 5):
        else_percent += cpu_time_percent[i]
    try:
        cpu_freq = psutil.cpu_freq()
    except AttributeError:
        cpu_freq = None
    if chart == 'line':
        datas = UserCpuPercent.objects.order_by('-id')[:30]   ##折线图显示最新30条记录
        return render(request, 'host/cpu-line.html', locals())
    elif chart == 'pie':
        return render(request, 'host/cpu-pie.html', locals())
    return render(request, 'host/cpu.html', locals())
def memory(request):
    pass
    return render(request,'host/memory.html',locals())

def disk(request):
    pass
    return render(request,'host/disk.html',locals())

def network(request):
    pass
    return render(request,'host/network.html',locals())

def process(request):
    pass
    return render(request,'host/process.html',locals())