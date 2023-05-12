
import requests

session = requests.Session()
session.trust_env = False

post_addr = 'http://p.njupt.edu.cn:801/eportal/?c=ACSetting&a=Login&wlanacip=10.255.252.150'


# IMPORTANT!!!
# In the next code line:

# replace "Bxxxxxxxx" and "YOUR_PASSWORD" to your Student ID and password
# replace "@xxxx" to "@cmcc" if you use the NJUPT_CMCC; to "@njxy" if you use NJUPT_CHINANET
# delete "@xxxx" if you use the WLAN NJUPT. (this is not tested)

post_data = { 'DDDDD': ",0,Bxxxxxxxx@xxxx", 'upass': "YOUR_PASSWORD" }
                           ######### ####             #############

session.post(post_addr, data = post_data)
