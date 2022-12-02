import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')

data = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(data)

comments = info['comments']

total = 0

for item in comments:
    total = total + int(item['count'])

print(total)
