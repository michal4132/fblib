import os, sys
from FB import FB

fb = FB()
fb.login("email", "pass")
wall = wall() # get wall html, TODO parse to plain text
print(len(wall))
fb.close()
