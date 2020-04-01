from pywinauto import Application  #导包
import time

app = Application().start("notepad.exe")  #打开程序
time.sleep(3)
win_ckts = app["无标题-记事本"]   #打开程序窗口
time.sleep(3)
win_ckts.print_control_identifiers()  #通过print_control_identifiers()这个方法，来获取这个窗口下的直接子控件