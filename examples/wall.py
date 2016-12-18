import os, sys
from FB import FB

fb = FB()
fb.login("email", "pass") # password must be encoded to base64
wall = fb.wall() # get wall html, TODO parse to plain text
print(len(wall))
fb.close()
