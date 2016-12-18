import os, sys
from FB import FB

fb = FB(0.5) # timeout
fb.login("email", "pass") # password must be encoded to base64
friends = fb.all_friends() # list friends from your account
friends_from = fb.friends_from_id(4) # list zuck's friends
print(len(friends))
print(len(friends_from))
fb.close()
