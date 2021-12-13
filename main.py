# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import paramiko
import os

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    ssh = paramiko.SSHClient()     # 创建SSH对象
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())     # 允许连接不在know_hosts文件中的主机
    ssh.connect(hostname='192.168.18.149', port=22, username='admin', password='admin')    # 连接服务器
    stdin, stdout, stderr = ssh.exec_command('get system interface')# 执行命令
    result = stdout.read()        # 获取命令结果
    ssh.close()    # 关闭连接
    print(result)
    for line in result:
        #line = line.strip()
        print(line)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
