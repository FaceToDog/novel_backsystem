import threading
import tkinter as tk
import ctypes
import os
from comtypes.client import CreateObject


class Application(tk.Tk):
    # 创建出主窗口
    def __init__(self):
        super().__init__()
        self.createUI()

    # 生成界面
    def createUI(self):
        # self.text = tk.Text(self)
        # self.text.pack()
        self.title('天龙八部脚本窗口')
        # 大小(720x480)，起始位置(40+40)
        self.geometry("720x480+40+40")
        dm = self.set_dm()
        # 注意lambda语句的作用！
        # Grid布局的常用属性有row(行)、column(列)、rowspan(组件占据行数)、columnspan(组件占据列数)
        tk.Button(self, text='登陆WeGame', command=lambda: self.thread_it(self.login_wegame(dm)))\
            .grid(row=0, column=0)
        tk.Button(self, text='测试输入文本信息', command=lambda: self.thread_it(self.login_input(dm))) \
            .grid(row=0, column=1)
        tk.Button(self, text='打图', command=lambda: self.thread_it(self.run_tu(dm))) \
            .grid(row=0, column=2)
        tk.Button(self, text='取消置顶', command=lambda: self.thread_it(self.del_up(dm))) \
            .grid(row=0, column=3)

    # 没有用self都是静态方法,静态方法是不涉及类内的
    @staticmethod
    def set_dm():
        print('正在免注册调用')
        dms = ctypes.windll.LoadLibrary('D:/游戏脚本/DmReg.dll')
        location_dmreg = os.getcwd() + '\dm.dll'
        dms.SetDllPathW(location_dmreg, 0)
        dm = CreateObject('dm.dmsoft')
        get_dm_connect = dm.Reg("hellodog866028ecd335241f55b1e00dc9220f0c", "6M1JaZihP")
        print('免注册调用成功 版本号为:', dm.Ver())
        if get_dm_connect == 1:
            print('注册登录成功，输出为:', get_dm_connect)
        else:
            print("注册失败!错误代码为", get_dm_connect)
            if get_dm_connect == -1:
                print('无法连接网络')
            elif get_dm_connect == -2:
                print('进程没有以管理员方式运行. (出现在win7 win8 vista 2008.建议关闭uac)')
            elif get_dm_connect == 0:
                print('失败 (未知错误)')
            elif get_dm_connect == 2:
                print('余额不足')
            elif get_dm_connect == 3:
                print('绑定了本机器，但是账户余额不足50元.')
            elif get_dm_connect == 4:
                print('注册码错误')
            elif get_dm_connect == 5:
                print('你的机器或者IP在黑名单列表中或者不在白名单列表中.')
            elif get_dm_connect == 6:
                print('非法使用插件. 一般出现在定制插件时，使用了和绑定的用户名不同的注册码.  也有可能是系统的语言设置不是中文简体,也可能有这个错误.')
            elif get_dm_connect == 7:
                print('你的帐号因为非法使用被封禁. ')
            elif get_dm_connect == 8:
                print('ver_info不在你设置的附加白名单中.')
            elif get_dm_connect == 77:
                print('机器码或者IP因为非法使用，而被封禁.')
            elif get_dm_connect == 777:
                print('同一个机器码注册次数超过了服务器限制,被暂时封禁.')
            elif get_dm_connect == -8:
                print('版本附加信息长度超过了20')
            elif get_dm_connect == -9:
                print('版本附加信息里包含了非法字母.')
        return dm

    @staticmethod
    def login_wegame(get_dm):
        # os 方法太占用资源，会造成窗口卡顿
        # os.startfile('"E:\游戏\wegame.exe"')
        get_dm.RunApp("E:\游戏\wegame.exe", 0)
        i = 1
        i_delay = 1000
        while get_dm.FindWindow("TWINCONTROL", "WeGame") == 0:
            get_dm.Delay(i_delay)
            if i == 10:
                print("程序没有找到!")
                break
            i += 1
        get_dm.Delays(2000, 3000)
        hwnd = get_dm.FindWindow("TWINCONTROL", "WeGame")
        login_address = get_dm.GetWindowRect(hwnd)
        get_dm.SetSimMode(1)
        # 置顶窗口
        get_window_first = get_dm.SetWindowState(hwnd, 8)
        if get_window_first != 1:
            print("窗口置顶失败，返回:", get_window_first)
        get_dm.MoveTo(login_address[0] + 790, login_address[1] + 243)
        get_dm.LeftDoubleClick()
        get_dm.Delays(2000, 3000)
        # 账号
        # 密码
        login_qq = "2291449865"
        login_password = "caonimade"
        get_dm.SendString2(hwnd, login_qq)
        get_dm.MoveTo(login_address[0] + 777, login_address[1] + 283)
        get_dm.LeftClick()
        get_dm.Delays(2000, 3000)
        get_dm.KeyPressStr(login_password, 20)
        get_dm.Delays(2000, 3000)
        get_dm.MoveTo(login_address[0] + 731, login_address[1] + 384)
        get_dm.LeftClick()

    @staticmethod
    def login_input(get_dm):
        hwnd = get_dm.FindWindow("TWINCONTROL", "WeGame")
        login_address = get_dm.GetWindowRect(hwnd)
        print(login_address)

    # 打包进线程（耗时的操作）
    @staticmethod
    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)   # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
        t.start()           # 启动
        # t.join()          # 阻塞--会卡死界面！

    @staticmethod
    def run_tu(get_dm):
        # 硬件驱动模拟
        get_dm.SetSimMode(1)
        # 设置真实模拟
        get_dm.EnableRealMouse(1, 20, 30)
        hwnd = get_dm.FindWindow("TianLongBaBuHJ WndClass", "")
        print(hwnd)
        i = 1
        i_delay = 1000
        while get_dm.FindWindow("TianLongBaBuHJ WndClass", "") == 0:
            get_dm.Delay(i_delay)
            if i == 10:
                print("程序没有找到!")
                break
            i += 1
        get_dm.Delays(2000, 3000)
        # 置顶窗口
        get_window_first = get_dm.SetWindowState(hwnd, 8)
        if get_window_first != 1:
            print("窗口置顶失败，返回:", get_window_first)
        # 获取当前窗口位置
        login_address = get_dm.GetWindowRect(hwnd)
        get_dm.Delays(2000, 3000)
        dm_ret = get_dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\任务.bmp", "000000", 0.9, 0)
        print(dm_ret)
        get_dm.MoveToEx(dm_ret[0] + 5, dm_ret[1] + 3, 5, 5)
        get_dm.LeftClick()
        get_dm.Delays(1000, 2000)
        dm_ret2 = get_dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\可接任务.bmp", "000000", 0.9, 0)
        get_dm.MoveToEx(dm_ret2[0] + 5, dm_ret2[1] + 3, 5, 5)
        get_dm.LeftClick()
        get_dm.Delays(1000, 2000)
        dm_ret3 = get_dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\打图任务.bmp", "000000", 0.9, 0)
        get_dm.MoveToEx(dm_ret3[0] + 5, dm_ret3[1] + 3, 8, 3)
        get_dm.LeftClick()
        get_dm.Delays(1000, 2000)
        dm_ret4 = get_dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\接图地点.bmp", "000000", 0.9, 0)
        get_dm.MoveToEx(dm_ret4[0] + 5, dm_ret4[1] + 3, 8, 3)
        get_dm.LeftClick()
        get_dm.Delays(5000, 10000)
        dm_ret5 = get_dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\接取任务.bmp", "000000", 0.9, 0)
        get_dm.MoveToEx(dm_ret5[0] + 5, dm_ret5[1] + 3, 8, 3)
        get_dm.LeftClick()


    @staticmethod
    def del_up(get_dm):
        hwnd = get_dm.FindWindow("TianLongBaBuHJ WndClass", "")
        get_window_first = get_dm.SetWindowState(hwnd, 9)
        if get_window_first != 1:
            print("窗口取消置顶失败，返回:", get_window_first)


app = Application()
app.mainloop()
