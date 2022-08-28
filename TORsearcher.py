from termcolor import colored
def torSearcher(url):
    # BEFORE YOU START - RUN tor.exe !!!!
    
    import requests
    import random
    def get_tor_session():
        session = requests.session()
        session.proxies = {'http':  'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        return session 

    # Make a request through the Tor connection
    # IP visible through Tor
    session = get_tor_session()
    #url = "http://httpbin.org/ip"
    #url = "http://x.onion/"


    #ua_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577"
    #,"Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36"
    #,"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36", "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
    #,"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"]
    #ua = random.choice(ua_list)
    #headers = {'User-Agent': ua}
    print("Getting ...", url)
    result = session.get(url).text
    # Above should print an IP different than your public IP
    # Following prints your normal public IP
    #print(requests.get("http://httpbin.org/ip").text)

    #>>> url = "http://x.onion/"
    #>>> url = url.replace("http://","")
    #>>> url = url.replace(".onion","")
    #>>> url = url.replace("/","")
    # or  u can use the name
    
    import string
    filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    with open(f"{filename}.txt","w+", encoding="utf-8") as newthing:
        newthing.write(result)

#url = "http://x.onion"
#torSearcher(url)

import sys
import os
programname = os.path.basename(sys.argv[0])
k = 0
try:
    thelist = sys.argv[1]
    print("Opening ...", thelist)
    with open(thelist, "r", encoding="utf-8") as newfile:
        data = newfile.readlines()
        
        for k in data:
            try :
                k = k.replace("\n","")
                k = "http://" + k
                torSearcher(k)
                text = colored('Site is Active', 'green', attrs=['reverse', 'blink'])
                print(text)
            except:
                text = colored('Site is inactive', 'red', attrs=['reverse', 'blink'])
                print(text)
            
                
        #p = 0
        # while True:
        # try:
        #     for k in data:
                
        # except:
        #     print("WEBSITE IS DOWN NO WORRIES")
        #     for k in data:
        #         k = k.replace("\n","")
        #         k = "http://" + k
        #         torSearcher(k)
                
            
except:
    print("Usage : {} <newlineSeperatedList.txt>".format(programname))

