# -*- coding: UTF-8 -*-
import sys
import paramiko
import time
import re

class Logger(object):
    def __init__(self, fileN='Default.log'):
        self.terminal = sys.stdout
        self.log = open(fileN, 'a')

    def write(self, message):
        '''print实际相当于sys.stdout.write'''
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

output_file = 'E:\\iplist1.txt'    #远程服务器地址
command_file = 'E:\\command.txt'   #巡检命令
file = open(output_file,"r",encoding='UTF-8')
print(file)
all = file.readlines()
print(all)
for ip in all:
    ip = ip.rstrip("\n")
    print(ip)
    port = 22     #端口
    username = "admin"   #用户名
    password = "admin"   #密码
    paramiko.util.log_to_file('E:\\ssh_connect_last.log')    #创建SSH连接日志文（只保留前一次连接的详细日志 以前的日志会自动被覆盖）
    ssh = paramiko.SSHClient()
    #ssh.load_system_host_keys()     #读取know_host
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #允许连接不在know_hosts文件中的主机
    ssh.connect(hostname=ip, port=port, username=username, password=password)   #建立SSH连接并执行命令
    conn = ssh.invoke_shell()
    command = open(command_file, "r")
    xunjian = command.readlines()
    for xunjian_command in xunjian:
        #print(xunjian_command)     #可打印命令#
        conn.send(xunjian_command)
        conn.send('\n')
        time.sleep(1)
        result = conn.recv(2048)
        results = result.replace(b'\r',b'')
        results = results.decode()
        print(results)   #打印标准输出
        print("-"*70)
        #results = Logger('E:\\xunjian.txt')
    ssh.close()