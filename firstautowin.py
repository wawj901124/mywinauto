from pywinauto import Application  #导包
import time
from pywinauto.keyboard import send_keys #对键盘操作

EXE_NAME = "ComMonitor.exe"
CHENGXU_NAME = "串口调试软件4.5"
SELECT_COM_NUM="COM1"


app = Application().start(EXE_NAME)  #打开程序
app.window()
time.sleep(3)
win_ckts = app[CHENGXU_NAME]   #打开程序窗口
time.sleep(3)
# win_ckts.print_control_identifiers()  #通过print_control_identifiers()这个方法，来获取这个窗口下的直接子控件

#获取控件文本内容
def get_Control_Text(control):
    # 获取当前端口选择内容的文本信息
    control_resouce_str = str(control.texts)

    print(control_resouce_str)
    control_resouce_str_list = control_resouce_str.split("'")
    print(control_resouce_str_list)
    control_text = control_resouce_str_list[1]
    print(control_text)
    return control_text




#点击COM1（端口选项）
select_com = win_ckts["ComboBox1"]
#获取当前端口选择内容的文本信息
# select_com_text_body = str(select_com.texts)
# print(select_com_text_body)
# select_com_text_body_list = select_com_text_body.split("'")
# print(select_com_text_body_list)
# select_com_text = select_com_text_body_list[1]
# print(select_com_text)

select_com_text = get_Control_Text(select_com)
print(select_com_text)
now_select_com_num = select_com_text.split("M")[1]  #工具当前选择的端口
print(now_select_com_num)
pre_select_com_num = SELECT_COM_NUM.split("M")[1]  #想要选择的端口
print(pre_select_com_num)

now_select_com_num_int = int(now_select_com_num)
pre_select_com_num_int = int(pre_select_com_num)

if now_select_com_num_int==pre_select_com_num_int: #如果相等则不进行操作
    pass
elif pre_select_com_num_int > now_select_com_num_int:  #如果预期比实际大，则点击后上一动然后按enter键
    cha = pre_select_com_num_int - now_select_com_num_int
    print(cha)
    print("即将点击")
    select_com.click
    # select_com.texts
    print("已经点击")
    for i in range(0,cha):
        send_keys("{VK_DOWN}")   #按向下键
        time.sleep(1)

    #按enter键
    send_keys("{VK_RETURN}")
    time.sleep(1)
    #再次获取控件文本
    select_com_text_hou = get_Control_Text(select_com)
    print("选择的端口为：%s"%select_com_text_hou)
    assert select_com_text_hou==SELECT_COM_NUM
else:
    cha = now_select_com_num_int - pre_select_com_num_int
    print(cha)
    print("即将点击")
    select_com.click()
    # select_com.texts
    print("已经点击")
    for i in range(0,cha):
        send_keys("{VK_UP}")   #按向上键
        time.sleep(1)

    #按enter键
    send_keys("{VK_RETURN}")
    time.sleep(1)
    #再次获取控件文本
    select_com_text_hou = get_Control_Text(select_com)
    print(select_com_text_hou)
    assert select_com_text_hou==SELECT_COM_NUM




time.sleep(3)
# print("即将点击")
# # select_com1.click()
# # select_com1.texts
# print("已经点击")
# time.sleep(3)
# win_ckts.print_control_identifiers()  #打印点击后的控件


# select_com1 = win_ckts["Static3"]
# time.sleep(3)
# # print("即将点击")
# # select_com1.click()
# # print("已经点击")
# # time.sleep(3)




