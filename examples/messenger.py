import os, sys,time
from fblib.FB import FB
import threading

run = True

fb = FB()
fb.login("email", "pass")
mid = "" #chat id (mid.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)
userid = "" # user id
tid = "" # second user id
def bg(mid):
    global run
    lastmsg = ""
    while run:
        msg = fb.get_lastest_msg(mid)
        if msg != lastmsg:
            print(msg[0]+": "+msg[1])
        lastmsg = msg
        time.sleep(1)

t = threading.Thread(target=bg, args=(mid,)).start()
while run:
    try:
        msg = input()
        fb.send_message(mid, userid, tid, msg)
    except KeyboardInterrupt:
        run = False
fb.close()
