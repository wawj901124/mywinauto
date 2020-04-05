# from pywinauto import Application  #导包
# import time
# from pywinauto.keyboard import send_keys #对键盘操作
#
# # EXE_NAME = "ComMonitor.exe"
# EXE_NAME = r"C:\Windows\System32\cmd.exe"
# # CHENGXU_NAME = "串口调试软件4.5"
# # SELECT_COM_NUM="COM1"
#
#
# app = Application().start(EXE_NAME)  #打开程序
import os
# a = r"cd C:\Program Files (x86)\Google\Chrome\Application"
# f = os.popen(a)
# print(f.read())
# #chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\Users\Administrator\PycharmProjects\wanwenyc\driver\chromedatadir"
# # cmdorder = 'cmd /k chrome'+' ' +'--remote-debugging-port=9222'+' '+ '--user-data-dir='+'"'+r'D:\Users\Administrator\PycharmProjects\wanwenyc\driver\chromedatadir'+'"'
# # cmdorder = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

cmdorder = 'cmd.exe /k run.bat'
print(cmdorder)
f = os.popen(cmdorder)
print(f.read().encode('gbk').decode('utf8'))

# import subprocess
# f=subprocess.Popen('netstat',shell=True)
