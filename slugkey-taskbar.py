import win32api
from win32gui import *
import win32con
import sys, os

import re

import pyhk
import time
from win32clipboard import *



def slugify_clipboard_string():

        # http://stackoverflow.com/questions/3827511/copying-and-pasting-from-to-clipboard-with-python-win32
        OpenClipboard() 
        contents = GetClipboardData(win32con.CF_TEXT) # get clipboard data

        # fix the contents here
        fixed_name = re.sub(r'[^a-zA-Z0-9\.]+', '-', contents)
        
        # put the fixed string back on the clipboard
        EmptyClipboard()
        SetClipboardData(win32con.CF_TEXT, fixed_name)
        CloseClipboard()

        # paste the clipboard
        # http://code.activestate.com/lists/python-list/584186/
        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
        win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
        time.sleep(0.05)
        win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
        
        del fixed_name, contents


class MainWindow:

    def __init__(self):
        msg_TaskbarRestart = RegisterWindowMessage("TaskbarCreated");
        message_map = {
                msg_TaskbarRestart: self.OnRestart,
                win32con.WM_DESTROY: self.OnDestroy,
                win32con.WM_COMMAND: self.OnCommand,
                win32con.WM_USER+20 : self.OnTaskbarNotify,
        }

        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbarDemo"
        wc.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW;
        wc.hCursor = LoadCursor( 0, win32con.IDC_ARROW )
        wc.hbrBackground = win32con.COLOR_WINDOW
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        classAtom = RegisterClass(wc)

        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow( classAtom, "SlugKey", style, \
                0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                0, 0, hinst, None)
        UpdateWindow(self.hwnd)
        self._DoCreateIcons()

        #create pyhk class instance
        hot = pyhk.pyhk()
         
        #add hotkey
        hot.addHotkey(['Ctrl','F12'],slugify_clipboard_string)
         
        #start looking for hotkey.
        hot.start()

    def _DoCreateIcons(self):

        # Try and find a custom icon
        hinst =  GetModuleHandle(None)
        # iconPathName = os.path.abspath(os.path.join( os.path.split(sys.executable)[0], "pyc.ico" ))
        iconPathName = os.path.join(os.path.dirname(__file__), 'pyc.ico')
        if not os.path.isfile(iconPathName):

            # Look in the source tree.
            iconPathName = os.path.abspath(os.path.join( os.path.split(sys.executable)[0], "..\\PC\\pyc.ico" ))
        if os.path.isfile(iconPathName):
            icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            hicon = LoadImage(hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags)
        else:
            print "Can't find a Python icon file - using default"
            print iconPathName
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)

        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "SlugKey - Ctrl+F12 to create slug from clipboard text")
        Shell_NotifyIcon(NIM_ADD, nid)



    def OnRestart(self, hwnd, msg, wparam, lparam):
        self._DoCreateIcons()



    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0) # Terminate the app.



    def OnTaskbarNotify(self, hwnd, msg, wparam, lparam):
        #if lparam==win32con.WM_LBUTTONUP:
            # print "You clicked me."
        if lparam==win32con.WM_LBUTTONDBLCLK:
            # print "You double-clicked me - goodbye"
            DestroyWindow(self.hwnd)
        elif lparam==win32con.WM_RBUTTONUP:
            # print "You right clicked me."
            menu = CreatePopupMenu()
            # AppendMenu( menu, win32con.MF_STRING, 1023, "Display Dialog")
            AppendMenu( menu, win32con.MF_STRING, 1024, "Convert clipboard text to slug")
            AppendMenu( menu, win32con.MF_STRING, 1025, "Exit" )
            pos = GetCursorPos()

            # See http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winui/menus_0hdi.asp
            SetForegroundWindow(self.hwnd)
            TrackPopupMenu(menu, win32con.TPM_LEFTALIGN, pos[0], pos[1], 0, self.hwnd, None)
            PostMessage(self.hwnd, win32con.WM_NULL, 0, 0)
        return 1



    def OnCommand(self, hwnd, msg, wparam, lparam):
        id = LOWORD(wparam)
        if id == 1023:
            import win32gui_dialog
            win32gui_dialog.DemoModal()
        elif id == 1024:
            slugify_clipboard_string()
        elif id == 1025:
            print "Goodbye"
            DestroyWindow(self.hwnd)
        else:
            print "Unknown command -", id



def main():
    w=MainWindow()
    PumpMessages()



if __name__=='__main__':
    main()

