from slackMonitor import slackMonitor
from sys import argv
import logging

USERNAME = argv[1]
USERPASSWORD = argv[2]
MSG = argv[3]

mySlack = slackMonitor('https://arris.slack.com/')
mySlack.login(USERNAME, USERPASSWORD)
mySlack.channel('CC04J4E3V')
mySlack.sendMessage(MSG)
