import time
import tkinter as tk   # 窗口模块
import main
import os
import threading    # 线程任务模块
import 线程任务模块 as thding


def set_tk():
    # 创建窗口
    root = tk.Tk()
    root.title('天龙八部脚本窗口')
    # 大小(720x480)，起始位置(40+40)
    root.geometry("720x480+40+40")
    # 在点击时执行操作
    # 注册大漠
    dm = main.set_dm()

    def my_click(get_dm):
        main.moveto_top(get_dm)

    # Btn = tkinter.Button(容器，text=‘按钮上的文字’)
    but = tk.Button(root, text='移动鼠标', command=lambda: my_click(dm))
    but2 = tk.Button(root, text='登陆WeGame', command=lambda: thding.MyThread(thding.login_wegame(dm)))
    # Pack的常用属性有side和fill
    # Side属性：其取值为top、bottom、left和right，分别表示组件排列在上、下、左、右的位置。默认为top.
    # Fill属性：其取值为x、y、both, 分别表示填充x（水平）或y（垂直）方向的空间。
    but.pack()
    but2.pack()
    root.mainloop()




set_tk()