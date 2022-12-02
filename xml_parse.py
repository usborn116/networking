import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')

data = urllib.request.urlopen(url, context=ctx).read()
xml = ET.fromstring(data)
total = 0
lst = xml.findall('comments/comment')
for num in lst:
    total = total + int(num.find('count').text)

print(total)