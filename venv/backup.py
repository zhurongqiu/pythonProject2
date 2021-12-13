import xlrd
import paramiko
import time

def ssh_SW(name,ip):
    now = time.strftime("%Y%m%d", time.localtime(time.time()))
    trans = paramiko.Transport((ip, 22))
    trans.connect(username='admin', password='admin')
    ssh = paramiko.SSHClient()
    ssh._transport = trans
    stdin, stdout, stderr = ssh.exec_command('save')
    print(stdout.read().decode())
    stdin, stdout, stderr = ssh.exec_command('tftp 192.168.18.1 put startup.cfg ' + name + '-' + now + '.cfg')
    print(stdout.read().decode())
    trans.close()

def main():
    workbook = xlrd.open_workbook('./sw.xls')
    sheet = workbook.sheet_by_name('sw')
    count = sheet.nrows
    for i in range(count-1):
        i = i + 1
        rows = sheet.row_values(i)
        name = rows[0]
        ip = rows[1]
        ssh_SW(name,ip)

if __name__=="__main__":
    main()
