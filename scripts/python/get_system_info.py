#!/usr/bin/python
#coding=utf-8

__author__ = 'singo'
__datetime__ = '2019/4/9 2:51 PM '


import subprocess
import time
import psutil
import os
from datetime import datetime


def get_CPU():
    '''
    us: 用户空间占用CPU的百分比
    sy: 内核空间占用CPU的百分比
    ni: 改变过优先级的进程占用CPU的百分比
    id: 空闲CPU百分比
    wa: IO等待占用CPU的百分比
    hi: 硬中断占用CPU的百分比
    si: 软中断占用CPU的百分比
    st: 虚拟化环境中运行的其他操作系统所花费的时间
    '''
    _cpu_times_percent = psutil.cpu_times_percent()

    value_dic = {
        'us': _cpu_times_percent.user,
        'sy': _cpu_times_percent.system,
        'ni': _cpu_times_percent.nice,
        'id': _cpu_times_percent.idle,
        'wa': _cpu_times_percent.iowait,
        'hi': _cpu_times_percent.irq,
        'si': _cpu_times_percent.softirq,
        'st': _cpu_times_percent.steal
    }

    return value_dic

def get_mem(action='memory'):
    if action == 'memory':
        mem = psutil.virtual_memory()
        value_dic = {
            'total': round(mem.total/1024, 0),
            'free': round(mem.free/1024, 0),
            'used': round(mem.used/1024, 0),
            'buff/cache': round((mem.buffers + mem.cached)/1024, 0)
        }
    else:
        mem = psutil.swap_memory()
        value_dic = {
            'total': round(mem.total/1024, 0),
            'free': round(mem.free/1024, 0),
            'used': round(mem.used/1024, 0),
            'buff/cache': 'N/A'
        }



    return value_dic

def get_process():
    shell_command = "top -bn 1 |grep 'Tasks'| awk '{print \" \" $2 \" \" $4 \" \" $6 \" \" $8 \" \" $10}'"
    sp = subprocess.Popen(shell_command, shell=True, stdout=subprocess.PIPE)

    output, error = sp.communicate()

    if sp.returncode != 0:
        value_dic = {}
    else:
        total, running, sleeping, stopped, zombie = output.decode('utf-8').split()
        value_dic = {
            'total': total,
            'running': running,
            'sleeping': sleeping,
            'stopped': stopped,
            'zombie': zombie
        }

    return value_dic

def get_load():
    load = os.getloadavg()
    boot_time = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
    hours = boot_time.seconds//3600
    mins = int(round(boot_time.seconds%3600/3600*60, 0))
    value_dic = {
        'up': '{} days {}:{}'.format(boot_time.days, hours, mins),
        'users': len(psutil.users()),
        'load1': load[0],
        'load5': load[1],
        'load15': load[2]
    }
    return value_dic

def ping():
    shell_command = "ping -c 1 114.114.114.114|grep 'icmp_seq=1'|awk '{print $7 \" \" $8}'"
    sp = subprocess.Popen(shell_command, shell=True, stdout=subprocess.PIPE)

    output, error = sp.communicate()

    if sp.returncode != 0:
        value_dic = {}
    else:
        value_dic = {
            'delay': output.decode('utf-8').strip('\n').split('=')[1]
        }
    return value_dic

def network_traffic():
    net_io_counters1 = psutil.net_io_counters()
    time.sleep(1)
    net_io_counters2 = psutil.net_io_counters()

    value_dic = {
        'RX': '%.1f' % ((net_io_counters2.bytes_recv - net_io_counters1.bytes_recv)/1024),
        'TX': '%.1f' % ((net_io_counters2.bytes_sent - net_io_counters1.bytes_sent)/1024)

    }
    return value_dic

def get_system_info():
    system_info = {
        'CPU': get_CPU(),
        'memory': get_mem(action='memory'),
        'swap': get_mem(action='swap'),
        'process': get_process(),
        'load': get_load(),
        'ping': ping(),
        'network': network_traffic(),
        'time': time.time()
    }

    return system_info

print(get_system_info())
