# sendsms_modem_zte_MF-823

# Sending SMS via modem ZTE MF823
###### For python 2.

```
#!/usr/bin/python

# coding: utf8

from time import gmtime, strftime	
import urllib
import pycurl
import sys

#host = '192.168.8.1'
host = '192.168.0.1'
port = '80'

reload(sys)
sys.setdefaultencoding('utf8')
text=sys.argv[1]
text=text.encode("utf-16-be")
msg="".join("{:02x}".format(ord(c)) for c in text)

#number = '+7***'
number=sys.argv[2]

time=strftime("%y;%m;%d;%H;%M;%S;+5", gmtime())

url = 'http://'+host+':'+port+'/goform/goform_set_cmd_process'
post = urllib.urlencode({'notCallback' : 'true', 'goformId' : 'SEND_SMS', 'isTest' : 'false','Number' : number, 'sms_time': time, 'MessageBody': msg, 'encode_type' : 'UNICODE', 'ID' : '-1'})
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.REFERER, 'http://'+host+':'+port+'/index.html')
c.setopt(pycurl.VERBOSE, 0)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, post)
c.perform()
print '\n'
```


###### For python 3.

```
#!/usr/bin/python

import sys
import time

import requests

host = "192.168.0.1"
port = "80"
# port = None

if port:
    origin = f"http://{host}:{port}"
else:
    origin = f"http://{host}"

text = sys.argv[1]
text = text.encode("utf-16-be")
msg = "".join("{:02x}".format(c) for c in text)

number = sys.argv[2]

time = time.strftime("%y;%m;%d;%H;%M;%S;%z", time.localtime())

url = f"{origin}/goform/goform_set_cmd_process"
headers = {
    "Referer": f"{origin}/index.html",
    "Origin": f"{origin}",
}
payload = {
    "isTest": "false",
    "goformId": "SEND_SMS",
    "notCallback": "true",
    "Number": number,
    "sms_time": time,
    "MessageBody": msg,
    "ID": "-1",
    "encode_type": "UNICODE",
}
r = requests.post(url, headers=headers, data=payload)
print(r.text)
```
###### Use:
```
$ python sms.py "любой текст" "+790......."
```
