import requests

session = requests.Session()
session.trust_env = False

session.post('http://p.njupt.edu.cn:801/eportal/?c=ACSetting&a=Logout&wlanacip=10.255.252.150')
