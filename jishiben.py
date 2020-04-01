from pywinauto import Application   # 导包
import time


def pywinauto_task():   # 定义一个自动化任务的函数
    for i in range(1, 6):   # 让这个任务执行指定次数，这里是5次
        app = Application().start('notepad.exe')   # 实例化一个对象，并启动指定的应用程序，start参数也可写入路径
        time.sleep(3)
        app['无标题-记事本'].MenuSelect('帮助->关于记事本')   # 在指定标题的窗口中，选择菜单
        time.sleep(3)
        app['关于“记事本”']['确定'].click()   # 在弹出的窗口中，定位确定按钮，并点击
        time.sleep(3)
        app['无标题-记事本'].MenuSelect('文件->另存为...')   # 打开记事本的另存为窗口
        time.sleep(3)
        file_name = '第' + str(i) + '个.txt'   # 定义好文件的名字
        time.sleep(3)
        app['另存为']['edit'].TypeKeys(file_name)   # 将文件名键入
        time.sleep(3)
        app['另存为']['保存'].click()   # 更改文件名之后保存
        time.sleep(3)
        app[file_name].edit.TypeKeys('hello\n', with_newlines=True)   # 在记事本窗口中写入内容，并换行
        time.sleep(3)
        app[file_name].edit.TypeKeys('这是第' + str(i) + '个文件')   # 写入第二行内容
        time.sleep(3)
        app.Notepad.MenuSelect('文件->退出')   # 选择菜单退出
        time.sleep(3)
        app['记事本']['保存'].click()   # 保存写好的记事本
        time.sleep(3)


if __name__ == '__main__':   # 执行此函数
    pywinauto_task()
