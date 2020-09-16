from urllib.parse import urlparse
import re

url = 'https://devalto.ruckuswireless.com/api/ui/t/b8ea91c52240473cada96e92d2f0cfc4/dashboard'

result = urlparse(url).path
#tId = re.search('t/.*/', url)
tId = re.findall('t/(.+)/', url)
print(tId[0])
