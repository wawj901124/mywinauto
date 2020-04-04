from pywinauto import Application  #导包
import time
from pywinauto.keyboard import send_keys #对键盘操作


from autoComMonitor.common import AutoCommon
from autoComMonitor.config.commonConfig import CommonConfig


class HandleCheck(object):
    def __init__(self,app_windows,check_control_name):
        self.auto_common = AutoCommon()
        #应用窗口
        self.APP_WINDOWS = app_windows
        #控件的定位
        self.CHECK_CONTROL_NAME = check_control_name

    #处理选项框被选中
    def handle_check(self):
        self.auto_common.time_delay(1)
        #获取文本控件
        edit_control = self.APP_WINDOWS[self.CHECK_CONTROL_NAME]
        edit_control.draw_outline(colour='green',thickness=2)
        """默认为在当前定位到的窗口或控件周围画出一条边界线，方便我们看出定位到了哪个控件
            colour:边界线的颜色，默认为绿
            thickness：线的粗细，默认为2
            fill：以何种方式填充矩形（没试过，详见源码base_wrapper.py）
            rect:根据坐标画出矩形（默认是在当前定位到的元素上画出一个矩形）
        """
        p = edit_control.get_properties()["texts"]
        print("属性值：")
        print("----------------------------------------")
        print(p)
        print("----------------------------------------")

        #点击
        edit_control.check()
        self.auto_common.time_delay(1)


class HandleClick(object):
    def __init__(self,app_windows,click_control_name):
        self.auto_common = AutoCommon()
        #应用窗口
        self.APP_WINDOWS = app_windows
        #控件的定位
        self.CLICK_CONTROL_NAME = click_control_name

    #处理点击
    def handle_click(self):
        self.auto_common.time_delay(1)
        #获取点击控件
        edit_control = self.APP_WINDOWS[self.CLICK_CONTROL_NAME]
        edit_control.draw_outline(colour='green', thickness=2)
        p = edit_control.get_properties()
        print("属性值：")
        print("----------------------------------------")
        print(p)
        print("----------------------------------------")
        #点击
        edit_control.click()
        self.auto_common.time_delay(1)



class HandleSendText(object):
    def __init__(self,app_windows,edit_control_name,input_text):
        self.auto_common = AutoCommon()
        #应用窗口
        self.APP_WINDOWS = app_windows
        #控件的定位
        self.EDIT_CONTROL_NAME = edit_control_name
        #文字编辑区要输入的内容
        self.INPUT_TEXT = input_text



    #处理发送数据
    def handle_send_text(self):
        #获取文本控件
        edit_control = self.APP_WINDOWS[self.EDIT_CONTROL_NAME]
        edit_control.draw_outline(colour='green', thickness=2)
        p = edit_control.get_properties()
        print("属性值：")
        print("----------------------------------------")
        print(p)
        print("----------------------------------------")
        #输入内容
        edit_control.type_keys(self.INPUT_TEXT)


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
        select_com.draw_outline(colour='green',thickness=2)
        p = select_com.get_properties()
        print("属性值：")
        print("----------------------------------------")
        print(p)
        print("----------------------------------------")
        select_com_text = self.auto_common.get_Control_Text(select_com,self.SPLIT_FLAG,int(self.SPLIT_LIST_INDEX))
        print(select_com_text)

        pre_select_com_text = self.SELECT_COM_NUM

        now_select_com_num_int = 0
        pre_select_com_num_int = 0

        #获取目前的选项位置
        select_list = self.auto_common.get_Control_Text_By_Properties(select_com)
        #删除列表第一项，因为第一项为选中的项
        del select_list[0]

        print("select_list:")
        print(select_list)
        select_list_len = len(select_list)
        # select_list_len = len(self.SELECT_LIST)
        for i in range(0,select_list_len):
            if select_com_text == select_list[i]:
                now_select_com_num_int = i
                break

        #获取预期选项的位置
        for i in range(0,select_list_len):
            if pre_select_com_text == select_list[i]:
                pre_select_com_num_int = i
                break

        print("目前选择的是第%d项"% now_select_com_num_int)
        print("需要选择的是第%d项" %  pre_select_com_num_int)

        #比较预期与现在的选项好决定上移动或下移动的次数
        if now_select_com_num_int == pre_select_com_num_int:  # 如果相等则不进行操作
            select_com_text_hou = self.auto_common.get_Control_Text(select_com, self.SPLIT_FLAG, int(self.SPLIT_LIST_INDEX))
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
            select_com_text_hou = self.auto_common.get_Control_Text(select_com, self.SPLIT_FLAG,
                                                                    int(self.SPLIT_LIST_INDEX))
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
            select_com_text_hou = self.auto_common.get_Control_Text(select_com, self.SPLIT_FLAG,
                                                                    int(self.SPLIT_LIST_INDEX))
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
        self.ERROR_DIALOG_NAME = "ComMonitor"
        self.APP = self.start_app()
        self.APP_WINDOWS = self.get_app_windows()



    # 打开程序
    def start_app(self):
        app = Application().start(self.EXE_NAME)  # 打开程序
        return app

    def get_error_app_windows(self):#打开错误提示弹框
        error_app_windows = self.APP[self.ERROR_DIALOG_NAME]
        return error_app_windows

    def show_error_windows(self):
        error_app = self.get_error_app_windows()
        error_app.print_control_identifiers()

    def is_exist_error_dialog(self):
        try:
            error_app = self.get_error_app_windows()
            error_dialog = error_app.print_control_identifiers()
            print("存在错误弹框：%s" % self.ERROR_DIALOG_NAME)
            print("返回True")
            return True
        except:
            print("返回False")
            return False

    def click_error_confirm(self):
        # 获取到错误提示框
        error_app = self.get_error_app_windows()
        # 获取到错误提示框中的确定按钮并点击
        confirm_button = error_app["确定"]
        confirm_button.click()

    # 打开程序窗口
    def get_app_windows(self):
        #死循环判断.判断是否弹出弹框ComMonitor，如果没有则继续，如果有则需要点击确定后继续
        while True:
            # if self.APP.window(title=self.CHENGXU_NAME,class_name="#32770").exists():
            if self.is_exist_error_dialog():
                # print("应用窗口（%s）未打开，请查看应用窗口(%s)是否打开" % (self.CHENGXU_NAME,self.CHENGXU_NAME))
                self.click_error_confirm()
                continue
            else:
                print("应用窗口（%s）已经打开"%self.CHENGXU_NAME)
                break
        app_windows = self.APP[self.CHENGXU_NAME]
        return app_windows

    #延时等待函数
    def time_delay(self,delaytime):
        delaytime_int = int(delaytime)
        time.sleep(delaytime_int)
        print("等待%s" % delaytime)

    def show_son_control(self):
        #通过print_control_identifiers()这个方法，来获取这个窗口下的直接子控件
        self.APP_WINDOWS.print_control_identifiers()

    #处理选择端口
    def handle_select_com(self):
        app_windows = self.APP_WINDOWS
        select_control_name = self.SELECT_CONTROL_NAME
        select_list = self.common_config.DuanKou_SELECT_LIST
        select_option = "COM7"
        split_flag = "'"
        split_list_index = 1
        hs = HandleSelect(app_windows,select_control_name,select_list,select_option,split_flag,split_list_index)
        hs.handle_select()

    #处理选择波特率
    def handle_select_botelv(self):
        app_windows = self.APP_WINDOWS
        select_control_name = "ComboBox2"
        select_list = self.common_config.BoTeLv_SELECT_LIST
        select_option = "9600"
        split_flag = "'"
        split_list_index = 1
        hs = HandleSelect(app_windows,select_control_name,select_list,select_option,split_flag,split_list_index)
        hs.handle_select()

    #处理选择数据位
    def handle_select_shujuwei(self):
        app_windows = self.APP_WINDOWS
        select_control_name = "ComboBox3"
        select_list = self.common_config.ShuJuWei_SELECT_LIST
        select_option = "8"
        split_flag = "'"
        split_list_index = 1
        hs = HandleSelect(app_windows,select_control_name,select_list,select_option,split_flag,split_list_index)
        hs.handle_select()

    #处理选择校验位
    def handle_select_jiaoyanwei(self):
        app_windows = self.APP_WINDOWS
        select_control_name = "ComboBox4"
        select_list = self.common_config.JiaoYanWei_SELECT_LIST
        select_option = "无"
        split_flag = "'"
        split_list_index = 1
        hs = HandleSelect(app_windows,select_control_name,select_list,select_option,split_flag,split_list_index)
        hs.handle_select()

    #处理选择停止位
    def handle_select_tingzhiwei(self):
        app_windows = self.APP_WINDOWS
        select_control_name = "ComboBox5"
        select_list = self.common_config.TingZhiWei_SELECT_LIST
        select_option = "1"
        split_flag = "'"
        split_list_index = 1
        hs = HandleSelect(app_windows,select_control_name,select_list,select_option,split_flag,split_list_index)
        hs.handle_select()

    #处理选择发送去1_手动发送编辑内容
    def handle_send_text_sdfsone(self):
        app_windows = self.APP_WINDOWS
        edit_control_name = "手动发送Edit1"
        input_text = "nihao"
        ht = HandleSendText(app_windows,edit_control_name,input_text)
        ht.handle_send_text()

    #处理选择发送去1_点击清空按钮
    def handle_click_qikongone(self):
        app_windows = self.APP_WINDOWS
        click_control_name = "清空Button1"
        hc =  HandleClick(app_windows,click_control_name)
        hc.handle_click()

    #处理选择发送去1_点击手动发送按钮
    def handle_click_shoudongfasongone(self):
        app_windows = self.APP_WINDOWS
        click_control_name = "手动发送Button1"
        hc =  HandleClick(app_windows,click_control_name)
        hc.handle_click()

    #处理发送和接受配置
    def handle_send_and_receive_config(self):
        #选择点击显示保存发送
        app_windows = self.APP_WINDOWS
        click_control_name = "CheckBox15"
        hc =  HandleCheck(app_windows,click_control_name)
        hc.handle_check()

        #选择点击显示保存时间
        app_windows = self.APP_WINDOWS
        click_control_name = "CheckBox5"
        hc =  HandleCheck(app_windows,click_control_name)
        hc.handle_check()

        #选择点击换帧行
        app_windows = self.APP_WINDOWS
        click_control_name = "CheckBox4"
        hc =  HandleCheck(app_windows,click_control_name)
        hc.handle_check()

    #处理接受内容定位
    def handle_receive_text(self):
        app_windows = self.APP_WINDOWS
        edit_control_name = "发帧数RICHEDIT"
        input_text = "jieshouzijie"
        ht = HandleSendText(app_windows,edit_control_name,input_text)
        ht.handle_send_text()

    #处理所有编辑内容,waican
    def handle_receive_text_wai(self):
        app_windows = self.APP_WINDOWS
        # edit_control_name = "Edit"
        # input_text = "jieshouzijie"
        f = open("zhushou", "r", encoding="utf8")
        f_context = f.read()
        f_context_list = f_context.split("\n")
        f_context_list_len = len(f_context_list)
        all_list = []
        for i in f_context_list:
            if "edit" in i.lower():
                if "[" in i:
                    end = i.split("|")[1]
                    # print(end)
                    # print(type(end))
                    new_end = eval(end)  # 将字符串类型转为列表类型
                    print(new_end)
                    # print(type(new_end))
                    for j in new_end:
                        all_list.append(j)

        print(all_list)

        for i in all_list:
            try:
                edit_control_name=i
                input_text = str(i)
                ht = HandleSendText(app_windows, edit_control_name, input_text)
                ht.handle_send_text()
                print("------------------输入内容----------------------")
                edit_control = self.APP_WINDOWS[edit_control_name]
                self.auto_common.get_Control_Text(edit_control, "'", 1)
            except:
                continue



    def close_app(self):
        self.APP.kill()


    def run_man(self):
        pass
        # self.get_app_windows()
        # self.show_error_windows()
        # self.time_delay(5)
        # self.show_error_windows()
        # self.is_exist_error_dialog()
        # self.time_delay(5)
        # self.is_exist_error_dialog()
        # self.click_error_confirm()
        # self.handle_select_com()
        # self.handle_select_botelv()
        # self.handle_select_shujuwei()
        # self.handle_select_jiaoyanwei()
        # self.handle_select_tingzhiwei()
        # self.handle_click_qikongone()
        # self.handle_send_text_sdfsone()
        # self.handle_click_shoudongfasongone()
        # self.handle_click_qikongone()
        # self.show_son_control()
        # self.time_delay(5)
        # print("-------------------------------------------------")
        # self.handle_send_and_receive_config()
        # print("-------------------------------------------------")
        # self.time_delay(5)
        # self.handle_send_and_receive_config()
        # self.handle_send_text_sdfsone()
        # self.handle_click_shoudongfasongone()

        # self.show_son_control()
        # self.close_app()
        # self.handle_receive_text()


if __name__ == "__main__":
    autos = AutoSelectCom()
    autos.handle_receive_text()


