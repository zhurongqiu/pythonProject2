#coding:utf-8

import paramiko

output_file = 'E:\\iplist.txt'
#远程服务器地址
file = open(output_file,"r",encoding='UTF-8')
print(file)
all = file.readlines()
print(all)
for ip in all:
    ip = ip.rstrip("\n")
    print(ip)
    #端口
    port = 22

    #用户名
    username = "admin"
    password = "admin"

    #创建SSH连接日志文（只保留前一次连接的详细日志 以前的日志会自动被覆盖）
    paramiko.util.log_to_file('E:\\ssh_connect_last.log')
    ssh = paramiko.SSHClient()

    #读取know_host
    #ssh.load_system_host_keys()

    #允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #建立SSH连接并执行命令
    ssh.connect(hostname=ip, port=port, username=username, password=password)
    stdin,stdout,stderr = ssh.exec_command('get system performance status')
    result = stdout.read()
    #打印标准输出
    print(result)
    print("-"*70)
    ssh.close()