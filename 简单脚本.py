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
        self.geometry("720x480+500+300")
        dm = self.set_dm()
        # 注意lambda语句的作用！
        # Grid布局的常用属性有row(行)、column(列)、rowspan(组件占据行数)、columnspan(组件占据列数)
        tk.Button(self, text='跑图', command=lambda: self.thread_it(self.run_tu(dm)))\
            .grid(row=0, column=0)
        tk.Button(self, text='接任务', command=lambda: self.thread_it(self.acc_tu(dm))) \
            .grid(row=0, column=1)
        tk.Button(self, text='杀气提醒', command=lambda: self.thread_it(self.chu_tu(dm))) \
            .grid(row=0, column=2)
        tk.Button(self, text='上下马', command=lambda: self.thread_it(self.ma_updown(dm))) \
            .grid(row=0, column=3)
        tk.Button(self, text='使用令牌', command=lambda: self.thread_it(self.use_lin(dm))) \
            .grid(row=0, column=4)
        tk.Button(self, text='切换前台', command=lambda: self.thread_it(self.loss_bwe(dm))) \
            .grid(row=0, column=5)
        tk.Button(self, text='切换后台', command=lambda: self.thread_it(self.set_bwe(dm))) \
            .grid(row=0, column=6)
        tk.Button(self, text='完成任务', command=lambda: self.thread_it(self.finash_tu(dm))) \
            .grid(row=0, column=7)
        tk.Button(self, text='完成任务最后', command=lambda: self.thread_it(self.finash_end(dm))) \
            .grid(row=0, column=8)
        tk.Button(self, text='绑定窗口', command=lambda: self.thread_it(self.get_bwe(dm))) \
            .grid(row=1, column=0)
        tk.Button(self, text='取消绑定', command=lambda: self.thread_it(self.del_up(dm))) \
            .grid(row=1, column=1)
        tk.Button(self, text='上下马', command=lambda: self.thread_it(self.ma_updown(dm))) \
            .grid(row=1, column=2)
        tk.Button(self, text='自动战斗', command=lambda: self.thread_it(self.auto_acc(dm))) \
            .grid(row=1, column=3)
        tk.Button(self, text='切换前台', command=lambda: self.thread_it(self.loss_bwe(dm))) \
            .grid(row=1, column=4)
        tk.Button(self, text='切换后台', command=lambda: self.thread_it(self.set_bwe(dm))) \
            .grid(row=1, column=5)
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
            print('注册登录成功!', get_dm_connect)
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

    # 打包进线程（耗时的操作）
    @staticmethod
    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)   # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
        t.start()           # 启动
        # t.join()          # 阻塞--会卡死界面！

    @staticmethod
    def del_up(get_dm):
        hwnd = get_dm.FindWindow("TianLongBaBuHJ WndClass", "")
        get_window_first = get_dm.SetWindowState(hwnd, 9)
        if get_window_first != 1:
            print("窗口取消置顶失败，返回:", get_window_first)
        unbw = get_dm.UnBindWindow()
        print("解绑", unbw)

    @staticmethod
    def get_bwe(dm):
        hwnd = dm.FindWindow("TianLongBaBuHJ WndClass", "")
        # print(hwnd)
        i = 1
        i_delay = 1000
        while dm.FindWindow("TianLongBaBuHJ WndClass", "") == 0:
            dm.Delay(i_delay)
            if i == 10:
                print("程序没有找到!")
                break
            i += 1
        dm.Delays(2000, 3000)
        # # 激活窗口
        get_window_first = dm.SetWindowState(hwnd, 1)
        # 设置前台点击模式
        dm_ret = dm.BindWindowEx(hwnd, "normal",
                                 "dx.mouse.position.lock.api|dx.mouse.position.lock.message|dx.mouse.focus.input.api|dx.mouse.focus.input.message|dx.mouse.clip.lock.api|dx.mouse.input.lock.api|dx.mouse.state.api|dx.mouse.state.message|dx.mouse.api|dx.mouse.cursor|dx.mouse.raw.input",
                                 "windows",
                                 "", 101)
        if get_window_first != 1:
            print("窗口激活失败，返回:", get_window_first)
        if dm_ret != 1:
            print("绑定失败，返回:", dm_ret)
        # 硬件驱动模拟
        dm.SetSimMode(1)
        # 设置真实模拟
        dm.EnableRealMouse(1, 20, 30)


    @staticmethod
    def run_tu(dm):
        hwnd = dm.FindWindow("TianLongBaBuHJ WndClass", "")
        # print(hwnd)
        i = 1
        i_delay = 1000
        while hwnd == 0:
            hwnd = dm.FindWindow("TianLongBaBuHJ WndClass", "")
            dm.Delay(i_delay)
            if i == 10:
                print("程序没有找到!")
                break
            i += 1
        dm.Delays(2000, 3000)
        # # 激活窗口
        get_window_first = dm.SetWindowState(hwnd, 1)
        if get_window_first != 1:
            print("窗口激活失败，返回:", get_window_first)
        # 获取当前窗口位置
        # login_address = dm.GetWindowRect(hwnd)
        # print(login_address)
        # dm.Delays(2000, 3000)
        # dm.MoveTo(233, 751)
        # dm.LeftClick()
        # dm.Delays(1000, 2000)
        # dm.MoveTo(394,148)
        # dm.LeftClick()
        # dm.Delays(1000, 2000)
        # dm.MoveTo(329,205)
        # dm.LeftClick()
        # dm.Delays(1000, 2000)
        # dm.MoveTo(413,385)
        # dm.LeftClick()
        dm.Delays(500, 1000)
        dm_ret = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\任务.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret[0] + 5, dm_ret[1] + 3, 5, 5)
        dm.LeftClick()
        dm.Delays(1000, 2000)
        dm_ret2 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\可接任务.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret2[0] + 5, dm_ret2[1] + 3, 5, 5)
        dm.LeftClick()
        dm.Delays(1000, 2000)
        dm_ret3 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\打图任务.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret3[0] + 5, dm_ret3[1] + 3, 8, 3)
        dm.LeftClick()
        dm.Delays(1000, 2000)
        dm_ret4 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\接图地点.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret4[0] + 5, dm_ret4[1] + 3, 8, 3)
        dm.LeftClick()
        # dm.Delays(5000, 10000)
        # dm_ret5 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\接取任务.bmp", "000000", 0.9, 0)
        # dm.MoveToEx(dm_ret5[0] + 5, dm_ret5[1] + 3, 8, 3)
        # dm.LeftClick()
        # while dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\接图地点.bmp", "000000", 0.9, 0) == -1:






    @staticmethod
    def acc_tu(dm):
        # dm.Delays(1000, 2000)
        # dm.MoveTo(83,203)
        # dm.LeftClick()
        # dm.Delays(1000, 2000)
        # dm.MoveTo(752,753)
        # dm.LeftClick()
        # dm.Delays(1000, 2000)
        # dm.MoveTo(846,271)
        # dm.LeftClick()
        # dm.Delays(1000, 2000)
        # dm.MoveTo(750,299)
        # dm.RightClick()
        # dm.Delays(1000, 2000)
        # dm.MoveTo(129,151)
        # dm.LeftClick()
        dm.Delays(50, 150)
        dm_ret = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\接取任务.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret[0] + 5, dm_ret[1] + 3, 5, 5)
        dm.LeftClick()
        dm.Delays(1000, 2000)
        dm_ret2 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\背包.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret2[0] + 5, dm_ret2[1] + 3, 5, 5)
        dm.LeftClick()
        dm.Delays(1000, 2000)
        dm_ret3 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\背包任务.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret3[0] + 5, dm_ret3[1] + 3, 8, 3)
        dm.LeftClick()
        dm.Delays(1000, 2000)
        dm_ret4 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\打图令牌.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret4[0] + 5, dm_ret4[1] + 3, 8, 3)
        dm.RightClick()
        # dm.Delays(1000, 2000)
        # dm_ret5 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\背包任务.bmp", "000000", 0.9, 0)
        # dm.MoveToEx(dm_ret5[0] + 5, dm_ret5[1] + 3, 8, 3)
        # dm.LeftClick()
        # dm.Delays(1000, 2000)
        # dm_ret6 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\打图令牌.bmp", "000000", 0.9, 0)
        # dm.MoveToEx(dm_ret6[0] + 5, dm_ret6[1] + 3, 8, 3)
        # dm.RightClick()
        dm.Delays(1000, 2000)
        dm_ret7 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\才能.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret7[0] - 30, dm_ret7[1] + 5, 8, 3)
        dm.LeftClick()



    @staticmethod
    def chu_tu(dm):
        # dm.Delays(1000, 2000)
        # dm.MoveTo(576,473)
        # dm.LeftClick()
        dm_ret7 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\杀气惩罚确定.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret7[0] - 7, dm_ret7[1] - 5, 8, 3)
        dm.LeftClick()

    @staticmethod
    def use_lin(dm):
        dm_ret2 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\背包.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret2[0] + 5, dm_ret2[1] + 3, 5, 5)
        dm.LeftClick()
        dm.Delays(1000, 2000)
        dm_ret3 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\背包任务.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret3[0] + 5, dm_ret3[1] + 3, 8, 3)
        dm.LeftClick()
        dm.Delays(1000, 2000)
        dm_ret4 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\打图令牌.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret4[0] + 5, dm_ret4[1] + 3, 8, 3)
        dm.RightClick()
        dm.Delays(2000, 3000)
        dm_ret5 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\自动战斗.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret5[0], dm_ret5[1], 3, 3)
        dm.LeftClick()

    @staticmethod
    def finash_tu(dm):
        # dm.Delays(1000, 2000)
        # dm.MoveTo(236,754)
        # dm.LeftClick()
        # dm.Delays(1000, 2000)
        # dm.MoveTo(451,383)
        # dm.LeftClick()
        dm.Delays(500, 1000)
        dm_ret = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\交易.bmp", "000000", 0.9, 0)
        # i = 0
        # while dm_ret == 0:
        #     dm_ret = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\任务.bmp", "000000", 0.9, 0)
        #     i = i+1
        #     print(dm_ret)
        #     if i == 20:
        #         print("任务这个图标没有找到！")
        #         break
        #     dm.Delays(20, 30)
        dm.MoveToEx(dm_ret[0] - 30, dm_ret[1] + 5, 5, 5)
        dm.LeftClick()
        dm.Delays(1000, 2000)
        dm_ret4 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\接图地点.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret4[0] + 5, dm_ret4[1] + 3, 8, 3)
        dm.LeftClick()

    @staticmethod
    def finash_end(dm):
        # dm.Delays(1000, 2000)
        # dm.MoveTo(78,203)
        # dm.LeftClick()
        # dm.Delays(1000, 2000)
        # dm.MoveTo(71,442)
        # dm.LeftClick()
        # dm.Delays(1000, 2000)
        # dm.MoveTo(71, 442)
        # dm.LeftClick()
        dm.Delays(50, 100)
        dm_ret = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\接取任务.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret[0] + 5, dm_ret[1] + 3, 5, 5)
        dm.LeftClick()
        dm.Delays(1000, 2000)
        dm_ret2 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\继续.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret2[0] + 5, dm_ret2[1] + 3, 5, 5)
        dm.LeftClick()
        dm.LeftUp()
        dm.Delays(1000, 2000)
        dm.MoveToEx(dm_ret2[0] + 200, dm_ret2[1] + 300, 5, 5)
        dm_ret3 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\完成.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret3[0] , dm_ret3[1] , 2, 1)
        dm.LeftClick()
        dm.LeftUp()
        # dm.Delays(1000, 2000)
        # dm.LeftClick()

    @staticmethod
    def ma_updown(dm):
        dm.Delays(1000, 2000)
        dm_ret3 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\上下马.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret3[0] + 10, dm_ret3[1] + 10, 8, 3)
        dm.LeftClick()

    @staticmethod
    def auto_acc(dm):
        dm.Delays(2000, 3000)
        dm_ret5 = dm.FindPic(0, 0, 2000, 2000, "D:\\游戏脚本\\img\\自动战斗.bmp", "000000", 0.9, 0)
        dm.MoveToEx(dm_ret5[0], dm_ret5[1], 3, 3)
        dm.LeftClick()

    @staticmethod
    def loss_bwe(dm):
        # 切换到前台
        dm.EnableBind(0)

    @staticmethod
    def set_bwe(dm):
        # 切换到后台
        dm.EnableBind(1)



app = Application()
app.mainloop()
