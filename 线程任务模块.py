import time
import os
import threading


class MyThread(threading.Thread):
    def __init__(self, func):
        super().__init__()
        self.func = func
        self.setDaemon(True)
        self.start()  # 在这里开始


def login_wegame(get_dm):
    os.startfile('"E:\游戏\wegame.exe"')
    time.sleep(8)
    hwnd = get_dm.FindWindow("TWINCONTROL", "WeGame")
    login_address = get_dm.GetWindowRect(hwnd)
    print(login_address)