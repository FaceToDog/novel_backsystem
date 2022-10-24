import ctypes
import os
from comtypes.client import CreateObject
# 创建大漠对象并返回


def set_dm():
    print('正在免注册调用')
    dms = ctypes.windll.LoadLibrary('D:/游戏脚本/DmReg.dll')
    location_dmreg = os.getcwd()+'\dm.dll'
    dms.SetDllPathW(location_dmreg, 0)
    dm = CreateObject('dm.dmsoft')
    get_dm_connect = dm.Reg("hellodog866028ecd335241f55b1e00dc9220f0c", "6M1JaZihP")
    print('免注册调用成功 版本号为:', dm.Ver())
    if get_dm_connect == 1:
        print('注册登录:', get_dm_connect)
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


def moveto_top(dm):
    dm.MoveTo(100, 100)


def fin_hwnd(dm):
    hwnd = dm.FindWindowByProcess("wegame.exe", "", "WeGame")
    print(hwnd)
    dm_ret = dm.GetClientSize(hwnd)
    print(dm_ret)


# dm = set_dm()
# fin_hwnd(dm)
# moveto_top(dm)