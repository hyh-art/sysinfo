import platform

from django.shortcuts import render
import psutil
import datetime
import os,platform
# Create your views here.

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
    pass
    return render(request,'host/user.html',locals())

def cpu(request):
    pass
    return render(request,'host/cpu.html',locals())

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