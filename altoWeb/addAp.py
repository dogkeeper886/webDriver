from sys import argv
from netDev import addNetDevice

if len(argv) != 6:
    print('[URL][USER_NAME][PASSWORD][DEV_NAME][DEV_SERIAL]')
    exit(1)

# env setting
url = argv[1]
uName = argv[2]
uPass = argv[3]
dNmae = argv[4]
dSerial = argv[5]

# go to url
web = addNetDevice(url)
web.login(uName, uPass)
web.addNetDevice('ap', dNmae, dSerial)