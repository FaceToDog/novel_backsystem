import os
import time
import win32gui
from ctypes import *

#需要右键pycharm以管理员身份运行
account = '1424404712'   #填写账号
pwd = 'tanglong'       #填写密码

os.startfile('"E:\游戏\wegame.exe"')
time.sleep(8)
a = win32gui.FindWindow("TWINCONTROL", "WeGame")
win32gui.SetForegroundWindow(a)
loginid = win32gui.GetWindowPlacement(a)
print(loginid)
print(loginid[4][0])
print(loginid[4][1])
time.sleep(1)


windll.user32.SetCursorPos(loginid[4][0]+790, loginid[4][1]+243)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#m = PyMouse()
#m.move(loginid[4][0]+790, loginid[4][1]+243)
#m.click(loginid[4][0]+790, loginid[4][1]+243, 1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
time.sleep(1)
k.tap_key(k.delete_key)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
time.sleep(1)
print(account)
k.type_string(account)
time.sleep(1)

windll.user32.SetCursorPos(loginid[4][0]+790, loginid[4][1]+283)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
time.sleep(5)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
time.sleep(1)
k.tap_key(k.delete_key)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

time.sleep(1)
k.type_string(pwd)
print(pwd)

#time.sleep(1)
#k.tap_key('i')

#time.sleep(1)
#win32api.keybd_event(65, 0, 0, 0)
#win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)

windll.user32.SetCursorPos(loginid[4][0]+710, loginid[4][1]+378)
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)



