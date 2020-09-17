from slack import slack
from sys import argv
from time import sleep
if len(argv) != 6:
    print('[USERNAME][PASSWORD][PVER][IDMID][ENV]')
    exit(1)

myUname = argv[1]
myPassword = argv[2]
myPver = argv[3]
myIdmId = argv[4]
myEnv = argv[5]

myAltobot = slack('https://arris.slack.com/')
myAltobot.login(myUname, myPassword)
myAltobot.channel('ruckus-alto-cicd')

text = '/alto-tenant setup {} {} {}'
myAltobot.runCommand(text.format(myPver, myIdmId, myEnv))
sleep(3)
myAltobot.findResult()
