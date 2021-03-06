#!/usr/bin/python

# coding: utf8

from time import gmtime, strftime
import urllib
import pycurl
import sys
import urllib.parse

#host = '192.168.8.1'
host = '192.168.0.1'
port = '80'

text=sys.argv[1]
text=text.encode("utf-16-be")
msg="".join("{:02x}".format(c) for c in text)

#number="+79***"
number=sys.argv[2]

time=strftime("%y;%m;%d;%H;%M;%S;+5", gmtime())

url = 'http://'+host+':'+port+'/goform/goform_set_cmd_process'
post = urllib.parse.urlencode({'notCallback' : 'true', 'goformId' : 'SEND_SMS', 'isTest' : 'false','Number' : number, 'sms_time': time, 'MessageBody': msg, 'encode_type' : 'UNICODE', 'ID' : '-1'})
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.REFERER, 'http://'+host+':'+port+'/index.html')
c.setopt(pycurl.VERBOSE, 0)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, post)
c.perform()
print("\n")
