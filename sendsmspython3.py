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
