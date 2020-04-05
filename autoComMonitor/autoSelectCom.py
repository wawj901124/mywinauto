from pywinauto import Application  #导包
import time
from pywinauto.keyboard import send_keys #对键盘操作


from autoComMonitor.common import AutoCommon

class AutoSelectCom(object):

    def __init__(self):
        self.IS_RESTART = False
        self.EXE_NAME = "ComMonitor.exe"
        self.CHENGXU_NAME = "串口调试软件4.5"
        self.SELECT_COM_NUM = "COM3"
        self.auto_common = AutoCommon()
        self.SELECT_CONTROL_NAME = "ComboBox1"
        self.APP = self.start_app()
        self.APP_WINDOWS = self.get_app_windows()

    # 打开程序
    def start_app(self):
        if self.IS_RESTART:
            app = Application().start(self.EXE_NAME)  # 打开程序
        else:
            app = Application().connect(path= self.EXE_NAME)
        return app

    # 打开程序窗口
    def get_app_windows(self):
        app_windows = self.APP[self.CHENGXU_NAME]
        return app_windows

    def time_delay(self,delaytime):
        delaytime_int = int(delaytime)
        time.sleep(delaytime_int)
        print("等待%s" % delaytime)

    #处理COM选择
    def handle_select_com(self):
        select_com = self.APP_WINDOWS[self.SELECT_CONTROL_NAME]
        select_com_text = self.auto_common.get_Control_Text(select_com,"'",1)
        print(select_com_text)
        now_select_com_num = select_com_text.split("M")[1]  # 工具当前选择的端口
        print(now_select_com_num)
        pre_select_com_num = self.SELECT_COM_NUM.split("M")[1]  # 想要选择的端口
        print(pre_select_com_num)

        now_select_com_num_int = int(now_select_com_num)
        pre_select_com_num_int = int(pre_select_com_num)

        if now_select_com_num_int == pre_select_com_num_int:  # 如果相等则不进行操作
            select_com_text_hou =  self.auto_common.get_Control_Text(select_com,"'",1)
            print("选择的端口为：%s"%select_com_text_hou)
        elif pre_select_com_num_int > now_select_com_num_int:  # 如果预期比实际大，则点击后上一动然后按enter键
            cha = pre_select_com_num_int - now_select_com_num_int
            print(cha)
            print("即将点击")
            select_com.click()
            # select_com.texts
            print("已经点击")
            self.auto_common.cha_click(cha, "{VK_DOWN}")  # 按向下键
            # 再次获取控件文本
            select_com_text_hou =  self.auto_common.get_Control_Text(select_com,"'",1)
            print("选择的端口为：%s"%select_com_text_hou)
            assert select_com_text_hou == self.SELECT_COM_NUM
        else:
            cha = now_select_com_num_int - pre_select_com_num_int
            print(cha)
            print("即将点击")
            select_com.click()
            # select_com.texts
            print("已经点击")
            self.auto_common.cha_click(cha,"{VK_UP}")  # 按向上键
            # 再次获取控件文本
            select_com_text_hou =  self.auto_common.get_Control_Text(select_com,"'",1)
            print("选择的端口为：%s"%select_com_text_hou)
            assert select_com_text_hou == self.SELECT_COM_NUM


    def run_man(self):
        self.handle_select_com()


if __name__ == "__main__":
    autos = AutoSelectCom()
    autos.run_man()

