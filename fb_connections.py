import os, sys
from FB import FB

fb = FB(0.5) # timeout
fb.login("email", "pass")
list = fb.friends_from_id(100003233321454)
print(list)
print(len(list))
fb.close()
