
import win32gui
import win32api
import win32con
import pyperclip
import win32ui
import time

mainWindow_name = u'YINCHUAN TERMINAL DVOR - Dual DVOR - SELEX Systems Integration Inc. PMDT'
MW_hwnd = win32gui.FindWindow(None, mainWindow_name)
main_menu = win32gui.GetMenu(MW_hwnd)
aim_menu = win32gui.GetSubMenu(main_menu, 2)
cmd_ID = win32gui.GetMenuItemID(aim_menu, 0)
win32gui.PostMessage(MW_hwnd, win32con.WM_COMMAND, cmd_ID, 0)
print("%x" % (MW_hwnd))

time.sleep(1)

dialog = win32gui.FindWindowEx(MW_hwnd, None, '#32770', None)
copy_btn = win32gui.FindWindowEx(dialog, None, 'Button', 'Copy')
print("%x" % (copy_btn))
win32gui.PostMessage(copy_btn, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
win32gui.PostMessage(copy_btn, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
# win32gui.PostMessage(dialog, win32con.WM_COMMAND, copy_btn, 0)
text = pyperclip.paste()
print(text)

# hwnd = win32gui.FindWindow(None, "YINCHUAN TERMINAL DVOR - Dual DVOR - SELEX Systems Integration Inc. PMDT")
# hwnd = win32gui.FindWindow(None, "PMDT")
# print(hwnd)
# name = 'hello'
# pyperclip.copy(name)
# print(pyperclip.paste())

# window_name = u'00080172'
# hwnd = win32gui.FindWindow(None, window_name)
# hwnd = u'00080172'
# menu = win32gui.GetMenu(hwnd)
# menu1 = win32gui.GetSubMenu(menu, 1)
# cmd_ID = win32gui.GetMenuItemID(menu1, 1)
# win32gui.PostMessage(hwnd, win32con.WM_COMMAND, cmd_ID, 0)

# #获取某个菜单的内容


# def get_menu_item_txt(menu, idx):
#     import win32gui_struct
#     mii, extra = win32gui_struct.EmptyMENUITEMINFO()  #新建一个win32gui的空的结构体mii
#     win32gui.GetMenuItemInfo(menu, idx, True, mii)   #将子菜单内容获取到mii
#     ftype, fstate, wid, hsubmenu, hbmpchecked, hbmpunchecked, dwitemdata, text, hbmpitem = win32gui_struct.UnpackMENUITEMINFO(mii)   #解包mii
#     return text


# for i in range(5):
#     print(get_menu_item_txt(menu, i))