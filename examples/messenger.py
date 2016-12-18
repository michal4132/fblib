import os, sys,time
from FB import FB
import threading

run = True

fb = FB()
fb.login("email", "pass") # password must be encoded to base64
mid = "" #chat id (mid.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)

def bg(mid):
    global run
    lastmsg = ""
    while run:
        msg = fb.get_lastest_msg(mid)
        if msg != lastmsg:
            print(msg[0]+": "+msg[1])
        lastmsg = msg
        time.sleep(0.5)

t = threading.Thread(target=bg, args=(mid,)).start()
while run:
    try:
        msg = input()
        fb.send_message(mid, msg)
    except KeyboardInterrupt:
        run = False
fb.close()
