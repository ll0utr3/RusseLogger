from scapy.all import sniff
from threading import Thread
from queue import Queue
q = Queue()
def listen(q):
    while 1:
        sniff(filter="icmp", prn=q.put, count=1)
def printp(q):
    while 1:
        packet = q.get().load.decode()
        with open("log.txt", "a") as f:
            f.write(packet)
Thread(target=listen, args=(q,)).start()
Thread(target=printp, args=(q,)).start()
