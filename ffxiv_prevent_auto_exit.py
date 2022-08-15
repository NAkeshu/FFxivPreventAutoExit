import time
import sys
import winsound
import ctypes

# Configurations
WaitTime = 20 * 60  # seconds
NeedAlert = True


"""
Reference:
1. [stackoverflow](https://stackoverflow.com/questions/12590145/how-to-simulate-raw-input-send-a-wm-input-message-to-an-application-the-right)
2. [key scan codes](https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-6.0/aa299374(v=vs.60)?redirectedfrom=MSDN)
"""

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002,
                        0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ClickKey(hexKeyCode):
    PressKey(hexKeyCode)
    time.sleep(0.2)
    ReleaseKey(hexKeyCode)
    time.sleep(0.5)


def main():
    while (True):
        time.sleep(WaitTime)
        hexKeyCode = 0x01  # esc scan key code
        ClickKey(hexKeyCode)
        ClickKey(hexKeyCode)

        if (NeedAlert):
            duration = 500  # milliseconds
            freq = 440  # Hz
            winsound.Beep(freq, duration)


if __name__ == "__main__":
    # if ctypes.windll.shell32.IsUserAnAdmin():
    #     main()
    # else:
    #     ctypes.windll.shell32.ShellExecuteW(
    #         None, "runas", sys.executable, __file__, None, 1)  # run script as administrator
    #     main()
    main()
