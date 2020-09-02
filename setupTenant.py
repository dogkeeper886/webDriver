import slack
import sys

if len(sys.argv) != 6:
    print('[USERNAME][PASSWORD][PVER][IDMID][ENV]')
    exit(1)

myUname = sys.argv[1]
myPassword = sys.argv[2]
myPver = sys.argv[3]
myIdmId = sys.argv[4]
myEnv = sys.argv[5]

myAltobot = slack.altobot()
myAltobot.login(myUname, myPassword)
myAltobot.channel('ruckus-alto-cicd')

text = '/alto-tenant setup {} {} {}'
myAltobot.runCommand(text.format(myPver, myIdmId, myEnv))
