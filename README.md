# SQL_Backups
#### 目标：将SQL数据库文件备份到服务器上
本地备份&上传到服务器 只保留7天
每天定时执行备份脚本

## 主要实现
1. 采用ftp协议传输，客户端python脚本直接调FTP库即可，服务器端需要先安装ftp服务
2. 通过服务器的IP地址和端口号进行连接传输
3. ftp传输需要登录的账户和密码需要在服务器端先创建  [参考链接](https://blog.csdn.net/weixin_32280593/article/details/116686808?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0.no_search_link&spm=1001.2101.3001.4242![image](https://user-images.githubusercontent.com/49605109/133544299-4a5961b9-83b4-43c5-b6b3-b8e0f83b9122.png))
4. 

## 遇到的bug
1. 一直连接不上服务器的原因可能是服务器的防火墙限制，腾讯云的服务器可以直接在控制台上管理防火墙加上允许21端口的规则
2. connectionrefusederror: [winerror 10061] 由于目标计算机积极拒绝，无法连接    可能是服务端还没有安装/启动ftp服务
3. ftp上传文件时报错：ftplib.error_perm: 550 Permission denied   修改ftp服务器配置文件中可写属性  [参考链接](https://blog.csdn.net/xiemanR/article/details/53325111)
4. ftp上传文件时报错：ftplib.error_perm: 553 Could not create file    当前登录的用户在ftp传输的文件夹没有写入权限 [参考链接](https://blog.csdn.net/weixin_30274627/article/details/98071355)

