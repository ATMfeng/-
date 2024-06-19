import requests
import time
import datetime
import socket
import uuid

def test():
    headers = {
    'Host': 'connect.rom.miui.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    }
    res=requests.get('http://connect.rom.miui.com/generate_204,headers=headers')
    return res



def weblogin(user,password,IP,mac):
    headers = {
    'Host':'219.226.127.250',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive',
    'Referer':'http://219.226.127.250/',
    'Upgrade-Insecure-Requests':'1'
    }
    
    
    
    
    url='http://219.226.127.250:801/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C2023005113&user_password=ZMro5364&wlan_user_ip=101.7.172.153&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=1092&lang=zh'.format(mac,IP,user,password)
    backinfo=requests.get(url,headers=headers)

def getip():
    return socket.gethostbyname(socket.gethostname())

def getmac():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return "-".join([mac[e:e+2] for e in range(0,11,2)])




count=0
ccc=0
dd=0
ee=0
while 1==1:
    time.sleep(0.25)
    if str(test())=='<Response [200]>':
        ccc+=1
        print("Lost Connect{}".format(ccc))
        if ccc==2:
            weblogin('账号','密码',str(getip()),str(getmac()))
            print('Relogin')
    else:
        if dd==20:
            dd=0
            ee+=1
            print("Internet is OK {}".format(ee))
        dd+=1
        ccc=0



