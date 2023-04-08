# can be run in termux. See https://github.com/termux/termux-app
# can't bypass proxy, so please turn tour proxy off if it is running
# however, other platform can bypass proxy, only android can't.

import os

ip_addr = os.popen("ifconfig | grep \"inet \" | grep -Fv 127.0.0.1 | awk \'{print $2}\'").read().strip()


import requests

post_addr = 'http://p.njupt.edu.cn:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=p.njupt.edu.cn&iTermType=1&wlanuserip=' + ip_addr + '&wlanacip=10.255.252.150&wlanacname=XL-BRAS-SR8806-X&mac=00-00-00-00-00-00&ip=' + ip_addr + '&enAdvert=0&queryACIP=0&loginMethod=1'

# replace Bxxxxxxxx and YOUR_PASSWORD as your actual Student ID and password in next section.
# replace njxy to cmcc if you use the Chine Mobile
# delete the suffix if you use school provided network, namely, NJUPT. (this line is experimental, and not tested)

post_data = { 'DDDDD': ",0,Bxxxxxxxx@njxy", 'upass': "YOUR_PASSWORD" }
                           ######### ####             #############

reauests.post(post_addr, data = post_data)