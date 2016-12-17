import bs4
import requests
import base64
import time

class FB():

    def __init__(self, timeout=1):
        self.timeout = timeout
    def login(self, email, password, headers = {'User-Agent': 'Mozilla/5.0'}):
        self.payload = {
            'action': 'login',
            'email': email,
            'pass': base64.b64decode(password) # encoding for people behind you
        }

        self.headers = headers
        self.c = requests.session()
        self.c.post('http://m.facebook.com/login.php', data=self.payload, headers=self.headers)

    def wall(self):
        self.response = self.c.get('http://m.facebook.com', headers=self.headers)
        return self.response.text

    def all_friends(self):
        friends = dict()
        fok = True
        fl = 0
        while fok:
            fnds = self.c.get("http://m.facebook.com/friends/center/friends/?ppk="+str(fl), headers=self.headers)
            fsoup = bs4.BeautifulSoup(fnds.text, "lxml")
            fok = False
            for f in fsoup.find_all('div', {'class': 'v bk'}):
                for id in f.find_all('a', {'class': 'bm'}):
                    fok = True
                    friends[id.text] = id['href'][31:].split('&')[0]
            fl+=1
            time.sleep(self.timeout)
        return friends
    def id2username(self, id):
        page = self.c.get('http://m.facebook.com/profile.php?id='+str(id), headers=self.headers)
        psoup = bs4.BeautifulSoup(page.text, "lxml")
        for fff in psoup.find_all('a', {'class': 'bw'}):
            if fff['href'].split('/')[2].startswith("friends"):
                fffurl = fff['href'].split("/")[1]
                return fffurl

    def friends_from_id(self, id):
        uname = self.id2username(id)
        e = True
        friends = dict()
        si = 0
        while e:
            fnds = self.c.get('http://m.facebook.com/'+uname+'/friends?startindex='+str(si), headers=self.headers)
            fsoup = bs4.BeautifulSoup(fnds.text, "lxml")
            e = False
            si+=24
            print(si)
            for f in fsoup.find_all('td', {'class': 'v s'}):
                for id in f.find_all('a'):
                    e = True
                    try:
                        href = id['href'][1:].split('?')[0]
                        if(href == "profile.php"): # working, but not perfect
                            friends[id.text] = id['href'][16:].split('&')[0]
                        elif(href.startswith("a/mobile/friends/add_friend.php") or href.startswith("notifications.php") or href.startswith("a/notifications.php")):
                            pass
                        else:
                            friends[id.text] = id['href'][1:].split('?')[0]
                    except:
                        friends[id.text] = "empty"
            time.sleep(self.timeout)
        return friends
    def close(self):
        self.c.close()
