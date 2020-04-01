from pywinauto import Application  #导包
import time
from pywinauto.keyboard import send_keys #对键盘操作


from autoComMonitor.common import AutoCommon
from autoComMonitor.config.commonConfig import CommonConfig


class HandleSendText(object):
    def __init__(self,app_windows,select_control_name,select_list,select_option,split_flag,split_list_index):
        #应用窗口
        self.APP_WINDOWS = app_windows
        #选项的定位
        self.SELECT_CONTROL_NAME = select_control_name
        #选项的列表
        self.SELECT_LIST = select_list
        #预期要选择的项
        self.SELECT_COM_NUM =select_option
        self.auto_common = AutoCommon()
        #选项内容分隔符号
        self.SPLIT_FLAG = split_flag
        #选项内容为分割后的第几项
        self.SPLIT_LIST_INDEX = split_list_index


    #处理发送数据
    def handle_send_text(self):
        #获取文本控件
        edit_control = self.APP_WINDOWS[self.SELECT_CONTROL_NAME]


        #输入内容
        pass




class HandleSelect(object):

    def __init__(self,app_windows,select_control_name,select_list,select_option,split_flag,split_list_index):
        #应用窗口
        self.APP_WINDOWS = app_windows
        #选项的定位
        self.SELECT_CONTROL_NAME = select_control_name
        #选项的列表
        self.SELECT_LIST = select_list
        #预期要选择的项
        self.SELECT_COM_NUM =select_option
        self.auto_common = AutoCommon()
        #选项内容分隔符号
        self.SPLIT_FLAG = split_flag
        #选项内容为分割后的第几项
        self.SPLIT_LIST_INDEX = split_list_index


    #处理COM选择
    def handle_select(self):
        #选项控件
        select_com = self.APP_WINDOWS[self.SELECT_CONTROL_NAME]
        select_com_text = self.auto_common.get_Control_Text(select_com,self.SPLIT_FLAG,int(self.SPLIT_LIST_INDEX))
        print(select_com_text)

        pre_select_com_text = self.SELECT_COM_NUM

        now_select_com_num_int = 0
        pre_select_com_num_int = 0

        #获取目前的选项位置
        select_list_len = len(self.SELECT_LIST)
        for i in range(0,select_list_len):
            if select_com_text == self.SELECT_LIST[i]:
                now_select_com_num_int = i
                break

        #获取预期选项的位置
        for i in range(0,select_list_len):
            if pre_select_com_text == self.SELECT_LIST[i]:
                pre_select_com_num_int = i
                break

        print("目前选择的是第%d项"% now_select_com_num_int)
        print("需要选择的是第%d项" %  pre_select_com_num_int)

        #比较预期与现在的选项好决定上移动或下移动的次数
        if now_select_com_num_int == pre_select_com_num_int:  # 如果相等则不进行操作
            select_com_text_hou =  self.auto_common.get_Control_Text(select_com,"'",1)
            print("选择的选项为：%s"%select_com_text_hou)
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
            print("选择的选项为：%s"%select_com_text_hou)
            assert str(select_com_text_hou) == str(self.SELECT_COM_NUM)
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
            print("选择的选项为：%s"%select_com_text_hou)
            assert str(select_com_text_hou) == str(self.SELECT_COM_NUM)


class AutoSelectCom(object):

    def __init__(self):
        self.auto_common = AutoCommon()
        self.common_config = CommonConfig()
        self.EXE_NAME = "ComMonitor.exe"
        self.CHENGXU_NAME = "串口调试软件4.5"
        self.SELECT_LIST = self.common_config.DuanKou_SELECT_LIST
        self.SELECT_COM_NUM = "COM6"
        self.SELECT_CONTROL_NAME = "ComboBox1"
        self.APP = self.start_app()
        self.APP_WINDOWS = self.get_app_windows()


    # 打开程序
    def start_app(self):
        app = Application().start(self.EXE_NAME)  # 打开程序
        return app

    # 打开程序窗口
    def get_app_windows(self):
        app_windows = self.APP[self.CHENGXU_NAME]
        return app_windows

    def time_delay(self,delaytime):
        delaytime_int = int(delaytime)
        time.sleep(delaytime_int)
        print("等待%s" % delaytime)

    def handle_select_com(self):
        app_windows = self.APP_WINDOWS
        select_control_name = self.SELECT_CONTROL_NAME
        select_list = self.common_config.DuanKou_SELECT_LIST
        select_option = "COM4"
        split_flag = "'"
        split_list_index = 1
        hs = HandleSelect(app_windows,select_control_name,select_list,select_option,split_flag,split_list_index)
        hs.handle_select()

    def handle_select_botelv(self):
        app_windows = self.APP_WINDOWS
        select_control_name = "ComboBox2"
        select_list = self.common_config.BoTeLv_SELECT_LIST
        select_option = "9600"
        split_flag = "'"
        split_list_index = 1
        hs = HandleSelect(app_windows,select_control_name,select_list,select_option,split_flag,split_list_index)
        hs.handle_select()

    def handle_select_shujuwei(self):
        app_windows = self.APP_WINDOWS
        select_control_name = "ComboBox3"
        select_list = self.common_config.ShuJuWei_SELECT_LIST
        select_option = "8"
        split_flag = "'"
        split_list_index = 1
        hs = HandleSelect(app_windows,select_control_name,select_list,select_option,split_flag,split_list_index)
        hs.handle_select()

    def handle_select_jiaoyanwei(self):
        app_windows = self.APP_WINDOWS
        select_control_name = "ComboBox4"
        select_list = self.common_config.JiaoYanWei_SELECT_LIST
        select_option = "无"
        split_flag = "'"
        split_list_index = 1
        hs = HandleSelect(app_windows,select_control_name,select_list,select_option,split_flag,split_list_index)
        hs.handle_select()

    def handle_select_tingzhiwei(self):
        app_windows = self.APP_WINDOWS
        select_control_name = "ComboBox5"
        select_list = self.common_config.TingZhiWei_SELECT_LIST
        select_option = "1"
        split_flag = "'"
        split_list_index = 1
        hs = HandleSelect(app_windows,select_control_name,select_list,select_option,split_flag,split_list_index)
        hs.handle_select()



    def run_man(self):
        self.handle_select_com()
        self.handle_select_botelv()
        self.handle_select_shujuwei()
        self.handle_select_jiaoyanwei()
        self.handle_select_tingzhiwei()


if __name__ == "__main__":
    autos = AutoSelectCom()
    autos.run_man()

