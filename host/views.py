from django.shortcuts import render

# Create your views here.

def index(request):
    pass
    return render(request,'/host/index.html',locals())

def user(request):
    pass
    return render(request,'/host/user.html',locals())

def cpu(request):
    pass
    return render(request,'/host/cpu.html',locals())

def memory(request):
    pass
    return render(request,'/host/memory.html',locals())

def disk(request):
    pass
    return render(request,'/host/disk.html',locals())

def network(request):
    pass
    return render(request,'/host/network.html',locals())

def process(request):
    pass
    return render(request,'/host/process.html',locals())