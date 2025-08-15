import time #键盘跑马灯 v1.00 2025-08-15 BJT 14:32:38
import itertools
import signal
import pyautogui #不知道为啥keyboard库死活调用不了scrolllock 所以我换个库来用
按键1 = "numlock"
按键2 = "capslock"
按键3 = "scrolllock"  #方便调试用 可以在这里修改字符名称
顺序 = input("请输入按键执行顺序 1为NumLock 2为CapsLock 3为ScrollLock 输入123为正序 321为倒序\n") 
speed =input("请输入期望的速度 单位秒")
lengthtest = len(顺序)  #通过len函数检测长度 防止输入非3位数字
if lengthtest == 3:
    print("")
else:
    print("输入长度无效")
    time.sleep(3)
    exit()
try:
    speedtype = float(speed)  # 尝试转换 若报错说明不是整数或浮点数
except ValueError:
    print("速度必须是数字！")
    time.sleep(3)
    exit()
if 顺序[0] == str(1):   #在Python中 读取变量的第一位应输入0
    实际按键1 = 按键1
else:
    if 顺序[0] == str(2):
        实际按键1 = 按键2
    else:
        if 顺序[0] == str(3):
            实际按键1 = 按键3
        else:
            typetest = type(顺序[0])  #typetest是用于校验类型的变量
            if typetest != "<class 'int'>":
                print("输入类型无效")
                time.sleep(3)
                exit()
if 顺序[1] == str(1):
    实际按键2 = 按键1
else:
    if 顺序[1] == str(2):
       实际按键2 = 按键2
    else:
        if 顺序[1] == str(3):
            实际按键2 = 按键3
        else:
            typetest = type(顺序[1])  
            if typetest != "<class 'int'>":
                print("输入类型无效")
                time.sleep(3)
                exit()
if 顺序[2] == str(1):
    实际按键3 = 按键1
else:    
    if 顺序[2] == str(2):
         实际按键3 = 按键2
    else:
        if 顺序[2] == str(3):
            实际按键3 = 按键3
        else:
            typetest = type(顺序[2])  
            if typetest != "<class 'int'>":
                print("输入类型无效")
                time.sleep(3)
                exit()
for _ in itertools.count():  #循环执行
    pyautogui.press(str(实际按键1))
    time.sleep(float(speed))
    pyautogui.press(str(实际按键2))
    time.sleep(float(speed))
    pyautogui.press(str(实际按键3))
    time.sleep(float(speed))

