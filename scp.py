# -*- coding: utf-8 -*-
import os
# 定义本地文件
localfile = '/home/linxin/Desktop/deepin使用心得.txt'
# 定义远程主机ip地址
remoteip = '110.42.130.67'
# 定义用户名
username = 'linxin'
# 定义用户密码
password = 'linxin'
# 定义远程传输文件地址
remotefoder = '/home/linxin/mysqlBackup/'
# linux下直接执行窗口命令
os.system('sshpass -p "%s" scp "%s" @ “%s "%s:%s"' % (password,localfile, username,remoteip, remotefoder) )