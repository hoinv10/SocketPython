from http.client import HTTPConnection
HTTPConnection.debuglevel = 1
from urllib.request import urlopen
import urllib.parse

a_url = 'http://103.1.209.157:8686/socket.io/?transport=polling&t=L-2Y25W'
response = urlopen(a_url)

header = response.headers.as_string()
body = response.read()
print("Header = ", header)
print("Body =", body)


hd = response.header()
print (hd)