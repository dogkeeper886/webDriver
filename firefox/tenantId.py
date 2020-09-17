from alto import altoWeb
from sys import argv

if len(argv) != 4:
    print('[URL][USER_NAME][PASSWORD]')
    exit(1)
# env setting
url = argv[1]
uName = argv[2]
uPass = argv[3]

# go to url
web = altoWeb(url)
web.login(uName, uPass)

print(web.tenantId())
