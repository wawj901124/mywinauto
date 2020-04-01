from pywinauto import Application  #导包
import time
from pywinauto.keyboard import send_keys #对键盘操作

class AutoCommon(object):

    def time_delay(self,delaytime):
        delaytime_int = int(delaytime)
        time.sleep(delaytime_int)
        print("等待%s" % delaytime)

    # 获取控件文本内容
    def get_Control_Text(self,control,splitflag,listindex):
        # 获取当前端口选择内容的文本信息
        control_resouce_str = str(control.texts)

        print(control_resouce_str)
        control_resouce_str_list = control_resouce_str.split(splitflag)
        print(control_resouce_str_list)
        control_text = control_resouce_str_list[listindex]
        print(control_text)
        return control_text

    def cha_click(self,cha,keyvalue):
        for i in range(0, cha):
            send_keys(keyvalue)  # 按向上键
            self.time_delay(1)
        # 按enter键
        send_keys("{VK_RETURN}")
        self.time_delay(1)
