
# -*- coding: utf-8 -*-
'''
 @project: Caculate
 @file: backups.py
 @function: 备份数据库文件，定时传输到服务器上
 @author:  linxin
 @date:  9/14/2021 - 8:54 PM
'''


# 导入 socket、sys 模块
import shutil
import socket
import sys
import os
import datetime
from ftplib import FTP
import time


# 连接ftp服务器function
def ftpconnect(host, username, password):
    print("begin connecting")
    ftp = FTP()
    ftp.connect(host, 21)
    ftp.login(username, password)
    print("connected successful")
    return ftp

#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    print("begin uploading")
    beginTime = time.time()
    # 设置ftp当前操作路径
    ftp.cwd('/home/linxin/mysqlBackup/')
    print(ftp.dir())
    bufsize = 1024
    print("准备打开本地文件")
    fp = open(localpath, 'rb')
    print(fp)
    print("准备写入文件")
    ftp.storbinary('STOR '+remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()
    endTime = time.time()
    print("uploaded successful")
    print("长传总共花费时间：", endTime - beginTime, 's')
    # 删除7天前的备份文件
    # 判断文件是否存在
    if (os.path.exists('/home/linxin/mysqlBackup/' + str(yesterdayFileName))):
        os.remove('/home/linxin/mysqlBackup/' + str(yesterdayFileName))
        print('移除7天前的备份')
    


# 定义/创建备份存储目录
backupDir ='F:\\mysqldb_backup'
if not os.path.exists(str(backupDir)):
    os.mkdir(str(backupDir))
# 切换目录
#os.chdir(str(backupDir))


# 获取当前工作目录，即当前python脚本工作的目录路径
currentDir = os.getcwd()
print('当前目录： '+currentDir)
sqlFilePath = str(currentDir)+'\\stisp.sql'
print('当前目录下sql文件路径： '+sqlFilePath)

# 定义备份当天和7天前的mysql名字
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=7)
todayFileName = str(today)+'mysqldb_backup.sql'
yesterdayFileName = str(yesterday)+'mysqldb_backup.sql'
print('todayFileName= ',todayFileName)
print('yesterdayFileName= ',yesterdayFileName)

backupFilePath = str(backupDir)+'\\'+str(todayFileName)
print('备份文件路径： '+backupFilePath)

# 拷贝文件
shutil.copyfile(sqlFilePath,backupFilePath)

if os.path.exists(str(backupDir)+'\\'+yesterdayFileName):
    os.remove(str(backupDir)+'\\'+yesterdayFileName)
    print('删除7天前的备份文件')

# 定义服务器的登录账户和密码
# 需要在服务器安装ftp后定义
username = 'linxin'
password = 'linxin'

# 定服务器中存储的路径
remotePath = '/home/linxin/mysqlBackup/'+str(todayFileName)
print('服务器地址: '+str(remotePath))
# 连接服务器
#print("begin connecting")
ftp = ftpconnect('110.42.130.67','linxin','linxin')
#print(" connected")

# 上传sql备份文件到服务器中
uploadfile(ftp, str(todayFileName), backupFilePath)
